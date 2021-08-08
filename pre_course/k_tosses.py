import random
import pandas as pd
import numpy as np


def simulate_tosses(k):
    count = {"heads": 0, "tails": 0}
    while (count['heads'] < 2):
        toss = random.choice(list(count.keys()))
        count[toss] = count[toss] + 1

    tosses = count['heads'] + count['tails']
    return tosses


ks = pd.Series(range(1, 100001)).apply(simulate_tosses)

values, counts = np.unique(ks, axis=0, return_counts=True)

# into a dict for presentation
result = {a: b for a, b in zip(values, counts)}
print(result)
