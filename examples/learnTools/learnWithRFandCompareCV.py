# -*- coding: utf-8 -*-
"""
Learn with Random-Forest and compare Cross-Validation methods
===============================================================

This example shows how to make a classification with different cross-validation methods.

"""

##############################################################################
# Import librairies
# -------------------------------------------

from museotoolbox.learnTools import learnAndPredict
from museotoolbox import crossValidation
from museotoolbox import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

##############################################################################
# Load HistoricalMap dataset
# -------------------------------------------

raster,vector = datasets.getHistoricalMap()
field = 'Class'
group = 'uniquefid'

##############################################################################
# Initialize Random-Forest
# ---------------------------

classifier = RandomForestClassifier()

##############################################################################
# Create list of different CV
# ---------------------------

CVs = [crossValidation.RandomCV(),
       crossValidation.LeavePSubGroupOut(),
       crossValidation.LeaveOneSubGroupOut(),
       StratifiedKFold() #from sklearn
       ]

kappas=[]

LAP = learnAndPredict()

for cv in CVs : 
        
    LAP.learnFromRaster(raster,vector,inField=field,inGroup=group,cv=cv,
                        classifier=classifier,param_grid=dict(n_estimators=[100,200]))
    print('Kappa for '+str(type(cv).__name__))
    cvKappa = []
    
    for kappa in LAP.getStatsFromCV(confusionMatrix=False,kappa=True):
        print(kappa)
        cvKappa.append(kappa)
    
    kappas.append(cvKappa)
    
    print(20*'=')

##########################
# Plot example


from matplotlib import pyplot as plt
plt.title('Kappa according to Cross-validation methods')
plt.boxplot(kappas,labels=[str(type(i).__name__) for i in CVs], patch_artist=True)
plt.grid()
plt.ylabel('Kappa')
plt.xticks(rotation=15)
plt.show()