# OPTIMADE Count Optimizer, Density Calc and ML example scripts

`optimadeCountOptimizer.py` is a Python script that tries to find an OPTIMADE query that gives a balanced count from multiple providers. Progress is logged continuously to a file on disk. One such log is `newNE15.pkl`.

`data_acquisition_and_density_calc.ipynb` is a Jupyter notebook that:
1. Uses the "best" OPTIMADE query found by `optimadeCountOptimizer.py` (and logged in `newNE15.pkl`)
2. downloads relevant data from multiple providers and saves it as a pandas DataFrame
3. calculates density for each entry and pickles it as `bestQryData.pkl`

`ML_notebook.ipynb`
1. Demonstrates the use of ML to predict density on data obtained from OPTIMADE providers (and pickled as `bestQryData.pkl`)
2. Shows improvement in $R^2$ when the model is trained using data from multiple providers.
3. Produces the figure used in the paper (saved as `highEntropyExample.pdf`)

`env.yml` can be used to create the conda environment in which the aforementioned have been tested to work.