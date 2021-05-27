import os
import urllib.request
import tarfile

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

import time


dataset_url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
housing_path = os.path.join('../datasets', 'housing')
housing_url = dataset_url + 'datasets/housing/housing.tgz'


def main():
	fetching_housing_data()
	housing = load_housing_data()
	# print(repr(housing.describe()))
	# housing.hist(bins=50, figsize=(8, 6))
	# plt.show()
	# print(repr(housing['ocean_proximity'].value_counts()))

	# random split
	# train, test = split_train_test(housing, 0.2)
	train_test_split(housing, test_size=0.2, random_state=42)


def split_train_test(data, ratio):
	# generate random indexes from 0 to len(data)
	shuffled_indices = np.random.permutation(len(data))
	test_dataset_size = int(len(data) * ratio)
	test_indices = shuffled_indices[:test_dataset_size]
	train_indices = shuffled_indices[test_dataset_size:]

	return data.iloc[train_indices], data.iloc[test_indices]
	

def fetching_housing_data(housing_url=housing_url, housing_path=housing_path):
	if not os.path.isdir(housing_path):
		os.makedirs(housing_path)
	tgz_path = os.path.join(housing_path, 'housing.tgz')
	urllib.request.urlretrieve(housing_url, tgz_path)
	housing_tgz = tarfile.open(tgz_path)
	housing_tgz.extract('housing.csv', path=housing_path)
	housing_tgz.close()


def load_housing_data(housing_path=housing_path):
	csv_path = os.path.join(housing_path, 'housing.csv')
	
	return pd.read_csv(csv_path)


if __name__ == '__main__':
	start_time = time.time()	
	main()
	end_time = time.time()
	print("Time elapsed: %.2f sec" % (end_time - start_time))


