"""This script performs queries for chemical formulae to all OPTIMADE APIs."""

if __name__ == "__main__":

    import pymongo as pm
    from optimade.client import OptimadeClient

    client = pm.MongoClient("mongodb://localhost:27017/optimade_example")
    collection = client.optimade_example.structures
    collection.create_index("immutable_id", unique=True)

    def insert_into_mongo(url, results):
        """Inserts data into a MongoDB collection."""
        prefix = results["meta"].get("provider", {}).get("prefix", None)
        for entry in results["data"]:
            formula = entry.pop("attributes")["chemical_formula_reduced"]
            entry["chemical_formula_reduced"] = formula
            entry["prefix"] = prefix
            entry["immutable_id"] = f"{url.scheme}://{url.host}{url.path}/{entry['id']}"
            try:
                collection.insert_one(entry)
            except pm.errors.DuplicateKeyError:
                continue

    download_structures = False

    client = OptimadeClient(
        exclude_providers=["nmd"],
        max_results_per_provider=-1,
        callbacks=[insert_into_mongo],
    )

    all_formulae = client.get(response_fields=["chemical_formula_reduced"])
