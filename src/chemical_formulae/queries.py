"""This script performs queries for chemical formulae to all OPTIMADE APIs."""

if __name__ == "__main__":
    import pymongo as pm
    from optimade.client import OptimadeClient
    from httpx import URL
    import urllib.parse

    client = pm.MongoClient("mongodb://localhost:27017/optimade_example")
    collection = client.optimade_example.structures
    collection.create_index("immutable_id", unique=True)
    collection.create_index("prefix")

    def insert_into_mongo(url, results):
        """Inserts data into a MongoDB collection."""
        prefix = results["meta"].get("provider", {}).get("prefix", None)
        url = URL(url)
        next_url = None
        duplicates = False
        # start = time.monotonic_ns()
        for entry in results["data"]:
            formula = entry.pop("attributes")["chemical_formula_reduced"]
            entry["chemical_formula_reduced"] = formula
            entry["prefix"] = prefix
            entry["immutable_id"] = f"{url.scheme}://{url.host}{url.path}/{entry['id']}"
            try:
                collection.insert_one(entry)
            except pm.errors.DuplicateKeyError:
                duplicates = True

        if duplicates:
            number_of_results_for_prefix = collection.count_documents(
                {"prefix": prefix}
            )
            suggested_page_offset = number_of_results_for_prefix - 1
            _next_url = results.get("links", {}).get("next")
            if isinstance(_next_url, dict):
                _next_url = _next_url.get("href")
            # If we have already reset the page offset once, don't do it again
            page_offset = urllib.parse.parse_qs(
                urllib.parse.urlparse(_next_url).query
            ).get("page_offset", [None])[0]

            if page_offset is None:
                return
            page_offset = int(page_offset)

            if _next_url and page_offset < 110:
                # Change the page offset to the suggested value using urllib.parse
                next_url = str(
                    URL(_next_url).copy_set_param("page_offset", suggested_page_offset)
                )

        if next_url:
            print(
                f"Overwriting next_url to {next_url}, existing results {suggested_page_offset + 1}"
            )
            return {"next": next_url, "advance_results": number_of_results_for_prefix}

        # (time.monotonic_ns() - start) / 1e9
        # print(f"Callback ran in {elapsed:.2f} s")

        return None

    download_structures = False

    client = OptimadeClient(
        max_results_per_provider=-1,
        include_providers=["mpds", "omdb", "aflow"],
        callbacks=[insert_into_mongo],
    )

    all_formulae = client.get(response_fields=["chemical_formula_reduced"])
