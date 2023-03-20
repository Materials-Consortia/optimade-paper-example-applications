from optimade.client import OptimadeClient
import numpy as np
import pandas as pd
import csv
from geneticalgorithm import geneticalgorithm as ga
from datetime import datetime
import time

fileName = input('Filename: ')
nelems = input('nelements>=')
#timeOut = int(input('Optimade timeout in seconds: '))
timeOut = 30
minNeedCount = int(input('Minumum needed count: '))
nDB = int(input('Number of databases in fitness cal: '))
nRunCount = 0

client = OptimadeClient(http_timeout=timeOut)
hasList = np.array(["Mn", "Cr", "Fe", "Co", "Ni", "Cu", "Ag", "W", "Mo", "Nb", "Al", "Cd", "Sn", "Pb", "Bi", "Zn", "Ge", "Si", "Sb", "Mg"])
necessaryFilterQuery = '''NOT elements HAS ANY "B", "Cl", "F", "H", "N", "O", "S", "Se", "C" AND nelements>='''+nelems


def printCountTable(res):
    for key, val in res['structures'][list(res['structures'].keys())[0]].items():
        print(str(val)+'\t'+key)

def fitCalc(res, nDB = nDB):
    countSer = pd.Series(res['structures'][list(res['structures'].keys())[0]])
    countTop = countSer.sort_values(ascending=False)[:nDB]
    printCountTable(res)
    if np.isnan(countTop.values.sum()):
        return 9999, [], []
    else:
        return (countTop.std()/countTop.mean()), list(countTop.index), countTop.values


def fitnessFunc(x, hasList=hasList, necessaryFilterQuery=necessaryFilterQuery, fileName = fileName):
    global nRunCount
    global data
    nRunCount = nRunCount+1
    hasSubList = hasList[np.array(x)>0.5]

    if len(hasSubList)==0:
        filterQuery = necessaryFilterQuery
    else:
        filterQuery = 'elements HAS ANY "'+'","'.join(hasSubList)+'" AND ' + necessaryFilterQuery
    time.sleep(3)
    res = client.count(filter=filterQuery)
    f, provList, countVals = fitCalc(res)
    print(f, countVals, provList)
    if len(countVals)>0:
        data = data.append({'Fitness Value':f, 'Count Mean':countVals.mean(), 'Count Std':countVals.std(), 'Count List':countVals, 'Input':np.array(x), 'Filter Query':filterQuery, 'Provider List':provList}, ignore_index=True)
    if nRunCount%10==0:
        data.to_pickle(fileName+'.pkl')
    return f


res = client.count(filter=necessaryFilterQuery) 
printCountTable(res)

newURLList = []
for key, val in res['structures'][list(res['structures'].keys())[0]].items():
    if type(val) == int and val>minNeedCount:
        newURLList.append(key)

client.base_urls = newURLList
print(newURLList)

data = pd.DataFrame(columns=['Fitness Value', 'Count Mean', 'Count Std', 'Count List', 'Input', 'Filter Query', 'Provider List'])
data.astype({'Fitness Value':float, 'Count Mean':'int64', 'Count Std':'int64', 'Count List':object, 'Input':object, 'Filter Query':str, 'Provider List': object})

algorithm_param = {'max_num_iteration': 3000,\
                   'population_size':10,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

model=ga(function=fitnessFunc,dimension=len(hasList),variable_type='bool', function_timeout = client.http_timeout*1.5, algorithm_parameters=algorithm_param)
model.run()
