import os
import urllib.request
import tarfile
import pandas as pd


dataset_url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
housing_path = os.path.join('../datasets', 'housing')
housing_url = dataset_url + 'datasets/housing/housing.tgz'

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


def main(): 
	fetching_housing_data()
	housing = load_housing_data()
	print(repr(housing.head()))


if __name__ == '__main__':
	main()


