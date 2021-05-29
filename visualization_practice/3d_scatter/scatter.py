import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error

# data: dataframe
data = pd.read_csv('objectFile.csv')

# divide each dimension's value
XY = data[['Input', 'Output']].values.reshape(-1, 2)
Z = data['Cost']

x = XY[:, 0]
y = XY[:, 1]
z = Z

# prepare data point for visualize model(2d)
num_point = 30
x_range = np.arange(min(x), max(x), (max(x) - min(x))/num_point)
y_range = np.arange(min(y), max(y), (max(y) - min(y))/num_point)

# made 2d-grid, num of points is num_point * num_point
# x_points, y_points are 2d-list
x_points, y_points = np.meshgrid(x_range, y_range)
model_viz = np.array([x_points.flatten(), y_points.flatten()]).T

# train using sklearn's LinR model, using ols, ols: ordinary least squares,
ols = linear_model.LinearRegression()
model = ols.fit(XY, Z)
predicted = model.predict(model_viz)

# evaluate model
r2 = model.score(XY, Z)

fig = plt.figure(figsize=(16, 5))

# 1, 3, 1: add subplot between 1 and 3, on 1
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
axes = [ax1, ax2, ax3]

# measure mean absolute error
mae = mean_absolute_error(Z, model.predict(XY))

for ax in axes:
  # plot experimental data
  ax.plot(x, y, z, color='black', zorder=15, linestyle='none', marker='o', alpha=0.5)
  # plot model
  ax.scatter(x_points.flatten(), y_points.flatten(), predicted, color='white', s=20, edgecolor='#70b3f0')

  ax.set_xlabel('Input RDD (MB)', fontsize=12)
  ax.set_ylabel('Output RDD (MB)', fontsize=12)
  ax.set_zlabel('Cost (sec)', fontsize=12)


ax1.view_init(elev=28, azim=120)
ax2.view_init(elev=4, azim=114)
ax3.view_init(elev=60, azim=165)

eq_str = '$: %.8fX_i + %.8fX_o + %.8f$, ' % (model.coef_[0], model.coef_[1], model.intercept_)
err_str = '$R^2 = %.3f, MAE = $%.3f sec' % (r2, mae)
fig.suptitle(eq_str + err_str, fontsize=15)
fig.tight_layout()

plt.show()
