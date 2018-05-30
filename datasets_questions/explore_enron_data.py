#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of persons
print "{} persons in the dataset".format(len(enron_data))

# Number of features
from statistics import mean, stdev
values = [len(person) for person in enron_data.values()]
print "Mean: {}, Std: {}".format(mean(values), stdev(values))
print "Std is 0, which means the answer is the mean: {}".format(
    int(mean(values)))

# Number of person of interest
pois = [person for person in enron_data.values() if person["poi"] == 1]
print "Number of POIs: {}".format(len(pois))

# Total value of the stock belonging to James Prentice
print "Total value of the stock belonging to James Prentice: {}".format(
    enron_data['PRENTICE JAMES']['total_stock_value'])

# How many email messages from Wesley Colwell
print "Number of emails sent from Wesley Colwell: {}".format(
    enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# Value of stock options exercised by Jeffrey K Skilling
print "Value of stock options exercised by Jeffrey K Skilling: {}".format(
    enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# How many people with a salary
print "Number of people with a salary: {}".format(
    len([p for p in enron_data.values() if p['salary'] != 'NaN']))

# How many known email address
print "Number of people with an email address: {}".format(
    len([p for p in enron_data.values() if p['email_address'] != 'NaN']))

# people_without_payments = len([p for p in enron_data.values() if p['total_payments'] != 'NaN']))

# How many people have NaN for their total payments
no_payment_count = len([p for p in enron_data.values()
                        if p['total_payments'] == 'NaN'])
print "Number of POIs without total payments: {}".format(no_payment_count)

print "Percentage of people without total payments: {:.2f}%".format(
    no_payment_count / float(len(enron_data)) * 100)

# How many POIs have NaN for their total payments
no_payment_poi_count = len([p for p in pois if p['total_payments'] == 'NaN'])

print "Number of POIs without total payments: {}".format(no_payment_poi_count)
