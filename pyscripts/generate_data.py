"""
Every even integer greater than 2 can be expressed as the sum of two primes
"""

import pandas as pd
import numpy as np

# parameters
n_max = int(1e6)
n_max = 1000*1000
n_every = 5000

# read primes
primes = np.loadtxt('data/primes.txt').astype(int)
primes_dict = {p: p for p in primes}


# generate counts
records = []
for x in range(4, n_max, 2):

    seqs = []
    counts = 0

    for p1 in primes:
        if p1 > x/2:
            break
        p2 = x - p1
        if p2 in primes_dict:
            seqs.append([p1, p2])
            counts += 1

    if x % n_every == 0:
        print('status: ', x, n_max, x/n_max)

        df = pd.DataFrame(records)
        df.to_csv('data/df_goldbach.csv', index=False)

    row = dict(x=x, counts=counts)
    records.append(row)

df = pd.DataFrame(records)
df.to_csv('data/df_goldbach.csv', index=False)
