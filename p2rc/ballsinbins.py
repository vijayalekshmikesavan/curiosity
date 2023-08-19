import numpy as np
import random
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt

def display_stats(trials, bins_rand, bins_p2rc):
    print(f'Number of trials = {trials}')
    fig, ax = plt.subplots(1, 2)
    sns.distplot(bins_rand, kde=False, ax=ax[0]).set(title='Random allocation')
    sns.distplot(bins_p2rc, kde=False, ax=ax[1]).set(title='Power of 2 random choices')
    plt.show()

bins_rand = np.zeros(1000).astype(int)
bins_p2rc = np.zeros(1000).astype(int)
trials = 0
try:
    while trials<1000000:
        r1 = random.randint(0, bins_rand.size-1)
        bins_rand[r1] = bins_rand[r1]+1

        r2 = random.randint(0, bins_p2rc.size-1)
        if( bins_p2rc[r1] <  bins_p2rc[r2]):
            bins_p2rc[r1] = bins_p2rc[r1] + 1
        else:
            bins_p2rc[r2] = bins_p2rc[r2] + 1

        trials = trials + 1
    display_stats(trials, bins_rand, bins_p2rc)
except KeyboardInterrupt:
    display_stats(trials, bins_rand, bins_p2rc)

