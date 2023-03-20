# Count Optimizer, Density Calc + ML example scripts

`optimadeCountOptimizer.py` is a script that tries to find an optimade query which gives a balanced count from multiple providers.

`densityCalcAndLearn.ipynb` is a jupyter notebook that:
1. uses the optimade query found with the previous script
2. downloads relevant data from multiple providers and saves it as a pandas DataFrame
3. calculates density of each entry
4. demonstrates the use of ML to predict density
5. Shows improvement in R^2^ when model is trained using data from multiple providers.

Both scripts are still being developed. Documentation/comments to be added.

