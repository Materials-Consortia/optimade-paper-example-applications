"""This script performs queries for high entropy alloy materials to all OPTIMADE APIs."""

if __name__ == "__main__":
    import json
    from pathlib import Path

    import pandas as pd
    from optimade.client import OptimadeClient
    from rich.console import Console
    from rich.table import Table

    console = Console()

    download_structures = False

    client = OptimadeClient(
        max_results_per_provider=1000
    )

    all_formulae = client.get(filter='chemical_formula_reduced="O2Si"')

    with open("all_SiO2.json", "w") as f:
        json.dump(all_formulae, f)
