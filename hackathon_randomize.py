import pandas as pd
import numpy as np
import random

threshold = 0.5
lower_rand = 0.5
upper_rand = 1.5
probability = random.uniform(0, 1)
file = 'df_balance_A.csv'


def round_sf(num, sig_fig):
    n = str(np.int64(num))
    if len(n) < sig_fig:
        return num
    count = 0
    answer = ""
    for i in n:
        if count == sig_fig:
            answer += '0'
        else:
            answer += i
            count = count + 1

    return answer


def find_sf(number):
    sf = 0
    for i in str(number):
        if i != '0' and i != '.':
            sf = sf + 1
    return sf


def match_dtype(match_this, anything):
    if type(match_this) is np.int64:
        return np.int64(anything)
    return np.float64(anything)


if probability < threshold:
    exit(0)

train = pd.read_csv('./hackathon_train/' + file)
test = pd.read_csv(file)
numeric_cols = train.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    if train[col].std() > 0 and col.find('Year') == -1 and col.find('Date') == -1:
        q75, q25 = np.percentile(train[col], [75, 25])
        iqr = q75 - q25
        if iqr > 0:
            this_sf = find_sf(test[col][0])

            fake_value = q25 + random.uniform(lower_rand, upper_rand) * iqr
            fake_value_rounded = round_sf(fake_value, this_sf)

            test[col][0] = match_dtype(train[col].max(), fake_value_rounded)

new_name = file[:-4] + '_modified.csv'
test.to_csv(new_name)
