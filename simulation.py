import warnings
warnings.filterwarnings("ignore")
from helper import calculate, generate_data
#input_dict = {"5": 1, "2": 6, "9":8,"1": 10,"7": 98,"4": 56}
import pandas

data = generate_data().poisson(75)
input_dict = dict(zip(data.index, data.S.values))
results = calculate(input_dict, verbose=False)
print(pandas.DataFrame(results.result, columns=["value", "utility"]).sort_values("utility", ascending=False))
import matplotlib.pyplot as plt
import seaborn as sns



ax = sns.distplot(data.S, hist=True, kde=False,
bins=int(180/9), color = 'darkblue', 
hist_kws={'edgecolor':'black'},
kde_kws={'linewidth': 4})

second_ax = ax.twinx()

sns.distplot(data.S, ax=second_ax,  kde=True, hist=False,
bins=int(180/9), color = 'darkblue', 
hist_kws={'edgecolor':'black'},
kde_kws={'linewidth': 4})
second_ax.set_yticks([])


# ax = plt.gca()
# fig2, ax2 = plt.subplots()
# sns.distplot(data, color='b')
# sns.distplot(data, ax=ax2, kde=False, norm_hist=False, color='b')
# ax.yaxis = ax2.yaxis

plt.show()

