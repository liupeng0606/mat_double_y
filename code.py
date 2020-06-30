# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')

x = ["20%", "40%", "60%", "80%"]
v = [0.432, 0.468, 0.493, 0.512]
a = [0.428, 0.458, 0.483, 0.532]

fig = plt.figure()
ax = fig.add_subplot(111)

lns1 = ax.plot(x, v, color='b', marker="o", label='Valence')
ax2 = ax.twinx()
lns2 = ax2.plot(x, a, color='r', marker="s", label='Arousal')


# added these two lines
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

ax.grid()
ax.set_xlabel("ratio of unlabeled data", fontsize=13)
ax.set_ylabel(r"Valence Pearson $\it{r}$", fontsize=13)
ax2.set_ylabel(r"Arousal Pearson $\it{r}$", fontsize=13)
ax2.set_ylim(0.4, 0.6, 0.1)
ax.set_ylim(0.3, 0.7, 0.05)
plt.show()
