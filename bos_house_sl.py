import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import visuals as vs
from sklearn.cross_validation import ShuffleSplit

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)

    
# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)

print np.amin(prices)
print np.amax(prices)
print np.mean(prices)
print np.median(prices)

par =  range(1,11);
params = {'max_depth':par}
print params



    
