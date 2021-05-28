import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# referenced from https://matplotlib.org/2.1.0/api/
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['figure.figsize'] = [20, 3.5]

data = pd.read_csv('data.csv')
label = data.iloc[:, 0].tolist()
# label = ['ALS', 'KM', 'SVM', 'LR', 'Bayes', 'LinR', 'RF', 'LDA', 'PCA', 'GBT', 'SVD', 'PR', 'NW', 'TS', 'GEOM']

p1_data = data.iloc[:, 1].tolist()
# p1_data = [0.6218118497, 0.9998249137, 0.5874426988, 0.6775329707, 0.7415608454, 0.263930788, 0.4382103472, 0.975012706,
#            0.597689194, 0.9570559916, 0.1471274331, 0.9980312369, 1.002548742, 0.9046619906, 0.6309574253]
p2_data = data.iloc[:, 2].tolist()
p3_data = data.iloc[:, 3].tolist()

# configurations
bar_width = 0.2
alpha = 1.00
dist = -0.1

index = np.arange(len(label))

fig = plt.figure()

# to draw straight line on y_axis=1
x_ = np.arange(-1, len(label)+1)
y_ = x_ * 0 + 1
plt.plot(x_, y_, 'black', linewidth=1.5, zorder=5)


p1 = plt.bar(index + dist - bar_width,  # x_loc
             p1_data,                   # values as list
             bar_width,                 # bar_width
             color='#1F4E79',
             alpha=alpha,               # transparency
             align='edge',
             edgecolor='black',
             zorder=3)

p2 = plt.bar(index + dist + bar_width * 0,
             p2_data,
             bar_width, 
             color='#9DC4E6',  
             alpha=alpha,
             align='edge',
             edgecolor='black',
             zorder=3)

p3 = plt.bar(index + dist + bar_width * 1,
             p3_data,
             bar_width, 
             color='#FFFFFF',  
             alpha=alpha,
             align='edge',
             edgecolor='black',
             zorder=3)


plt.ylabel('Normalized Execution Time', fontsize=20)

plt.ylim(0, 1.2)
plt.xlim([-1, len(label)])

plt.xticks(index + dist + bar_width * 0.5, label, fontsize=18)
plt.yticks(fontsize=18)
plt.tick_params(axis='x', which='both', bottom=False, top=False)

plt.legend((p1[0], p2[0], p3[0]), ('Static', 'CACAO', 'Best'), loc='lower left', fontsize=15, framealpha=1)

plt.grid(color='gray', linestyle='-', linewidth=0.5, zorder=-1, axis='y')

# save as pdf file
# plt.savefig(fname='perf.pdf', bbox_inches='tight', pad_inches=0.1)

plt.show()
