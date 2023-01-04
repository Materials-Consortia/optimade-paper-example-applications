"""This script performs queries for high entropy alloy materials to all OPTIMADE APIs."""

if __name__ == "__main__":
    import json

    import pandas as pd
    from optimade.client import OptimadeClient

    client = OptimadeClient()

    has_any_filter = '\
        elements HAS ANY "Mn", "Cr", "Fe", "Co", "Ni", "Cu", "Ag", "W", "Mo", "Nb", "Al", "Cd", "Sn", "Pb", "Bi", "Zn", "Ge", "Si", "Sb", "Mg" \
        AND \
        NOT elements HAS ANY "B", "C", "Cl", "F", "H", "N", "O", "S", "Se" \
        AND \
        nelements >= 5 \
        '

    has_any_results = client.count(filter=has_any_filter.strip())

    df = pd.DataFrame(has_any_results, index=[0])
    print(df)

    df.to_markdown("results_count_table.md")
    json.dump(has_any_results, open("data/has_any_hea_counts.json", "w"), indent=2)

    has_any_structures = client.get(
        filter=has_any_filter.strip(),
        response_fields=[
            "chemical_formula_reduced",
            "nsites",
            "cartesian_site_positions",
            "elements",
            "lattice_vectors",
        ],
        save_as="data/hea_structures.json",
    )
