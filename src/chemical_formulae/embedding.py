if __name__ == "__main__":
    import pymongo as pm 
    import pandas as pd
    from chem_wasserstein.ElM2D_ import ElM2D

    db = pm.MongoClient().optimade_example.structures

    cod_query = {"prefix": "cod",  "chemical_formula_reduced": {"$ne": None}}

    print(f"# of COD results {db.count_documents(cod_query)}")

    cod = db.find(cod_query)

    cod_df = pd.DataFrame(cod)


    mapper = ElM2D()

    mapper.fit(cod_df["chemical_formula_reduced"])

    breakpoint()
