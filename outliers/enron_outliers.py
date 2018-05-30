#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

# This code helps find the outlier in the data
max_salary = 0
person = ""
for k, v in data_dict.items():
    salary = v['salary']
    if salary != 'NaN' and salary > max_salary:
        max_salary = v['salary']
        person = k
print "Max salary is '{}' for '{}'".format(max_salary, person)

# Now let's remove it
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
