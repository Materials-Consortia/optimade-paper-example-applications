if __name__ == "__main__":
    import pymongo as pm 
    import pandas as pd
    from chem_wasserstein.ElM2D_ import ElM2D
    from sklearn.model_selection import train_test_split

    db = pm.MongoClient().optimade_example.structures

    cod_query = {"prefix": "cod",  "chemical_formula_reduced": {"$ne": None}}

    print(f"# of COD results {db.count_documents(cod_query)}")

    cod = db.find(cod_query, limit=1000)
    cod_df = pd.DataFrame(cod)
    train, test = train_test_split(cod_df, test_size=0.75)
    mapper = ElM2D(target="cpu", emd_algorithm="wasserstein")
    mapper.fit_transform(train["chemical_formula_reduced"].values.aslist(), how="UMAP")
    mapper.plot("umap.html")
