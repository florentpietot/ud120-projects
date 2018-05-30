#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    import numpy as np

    N = ages.shape[0]
    CUTOFF = 0.9
    num = int(CUTOFF * N)
    print "Will cut {} outliers".format(num)

    errors = abs(predictions.squeeze() - net_worths.squeeze())
    indexes = np.argsort(errors)[:num]
    data = zip(ages.squeeze(), net_worths.squeeze(), errors)
    cleaned_data = [e for i, e in enumerate(data) if i in indexes]

    return cleaned_data

