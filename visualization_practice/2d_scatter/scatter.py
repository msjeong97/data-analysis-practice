import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['figure.figsize'] = [16, 10]

def get_idx(name, labels):
  for idx in range(len(labels)):
    if labels[idx] == name:
      return idx
  return -1

data = pd.read_csv('textFile.csv')

workloads = data.iloc[:, 0].tolist()
labels = []

for workload_ in workloads:
  workload = workload_.split('_')[0]
  if workload not in labels:
    labels.append(workload)

num_workload = len(labels)

# size (MB)
# arr_x : size_list for each workload
# x : size_list for all plot's x idx
arr_x = []
x = []
for i in range(num_workload):
  arr_x.append([])

# cost (sec)
# arr_y : cost_list for each workload
# y : cost_list for all plot's y idx
arr_y = []
y = []
for i in range(num_workload):
  arr_y.append([])

size_list = data.iloc[:, 1].tolist()
cost_list = data.iloc[:, 2].tolist()
num_row = len(data)

for row_idx in range(num_row):
  workload_idx = get_idx(data.iloc[row_idx, 0].split('_')[0], labels)
  arr_x[workload_idx].append(data.iloc[row_idx, 1])
  arr_y[workload_idx].append(data.iloc[row_idx, 2])

  x.append(data.iloc[row_idx, 1])
  y.append(data.iloc[row_idx, 2])

markers = ['o', 'x', '^', 's', 'p', 'h', '+', 'D', '*', '1', 'v', '8', 'd', '_']
colors = ['blue', 'black', 'brown', 'fuchsia', 'gold', 'lime', 'lightblue', 'green', 'indigo', 'pink',
          'red', 'lavender', 'violet', 'khaki', 'silver', 'tomato', 'teal', 'cyan', 'azure', 'olive', 'maroon',
          'lightgreen', 'orangered', 'chocolate', 'darkgreen', 'magenta', 'orchid', 'salmon', 'sienna']

# plotting by workload
for workload_idx in range(len(labels)):
  plt.scatter(arr_x[workload_idx], arr_y[workload_idx], marker=markers[workload_idx], label=labels[workload_idx],
              color=colors[workload_idx], s=100)

# to find fittest polynomial model between linear model and cubic model
fittest_degree = 0
fittest_r2 = 0

for degree in range(1, 4):
  model = np.poly1d(np.polyfit(x, y, degree))
  r2 = r2_score(y, model(x))
  print('degree: {degree}, r2_score: {r2_score}'.format(degree=degree, r2_score=r2))
  if (fittest_r2 < r2):
    fittest_degree = degree
    fittest_r2 = r2

# coefficients
coeffs = np.polyfit(x, y, fittest_degree)
model = np.poly1d(coeffs)

# draw trend line
x_new = np.arange(min(x), max(x))
y_new = model(x_new)
plt.plot(x_new, y_new, color='black')

# graph configuration
plt.xlabel('Input RDD Size (MB)', fontsize=30)
plt.ylabel('Output Computing Cost (sec)', fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.legend(scatterpoints=1, loc='lower right', fontsize=10, ncol=3)

if(fittest_degree == 1):
  plt.title('%.3e$x$ + %.3e, $R^2$: %.3f' % (coeffs[0], coeffs[1], fittest_r2), fontsize=18)
elif(fittest_degree == 2):
  plt.title('%.3e$x^2$ + %.3e$x$ + %.3e, $R^2$: %.3f' % (coeffs[0], coeffs[1], coeffs[2], fittest_r2), fontsize=18)
elif(fittest_degree == 3):
  plt.title('%.3e$x^3$ + %.3e$x^2$ + %.3e$x$ + %.3e, $R^2$: %.3f' % (coeffs[0], coeffs[1], coeffs[2], coeffs[3],
                                                                     fittest_r2), fontsize=18)

plt.show()


