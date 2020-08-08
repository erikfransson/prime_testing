import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')


df = pd.read_csv('data/df_goldbach.csv')

fig, ax1 = plt.subplots(figsize=(16, 9))
ax1.plot(df.x, df.counts, 'o', ms=0.4)
ax1.set_xlim([0, df.x.max()])
ax1.set_ylim([0, df.counts.max()])
# xticks = ax1.get_xticks()
# xticklabs = ['{:.1e}'.format(x) for x in xticks]
# ax1.set_xticklabels(xticklabs)

ax1.set_xlabel('Number', fontsize=26)
ax1.set_ylabel('Number of representations', fontsize=26)

plt.show()
