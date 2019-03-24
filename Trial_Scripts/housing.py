from __future__ import division
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os, hashlib

fname = os.path.join('datasets','housing','housing.csv')
HOUSING_PATH = os.path.join('datasets','housing')
def load_housing_data(housing_path = HOUSING_PATH):
	csv_path = os.path.join(housing_path, "housing.csv")
	return pd.read_csv(csv_path)

def split_train_test_by_id(data,test_ratio, id_column, hash = hashlib.md5):
	ids = data[id_column]
	in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
	return data.loc[~in_test_set], data.loc[in_test_set]

def test_set_check(identifier, test_ratio, hash):
	return hash(np.int64(identifier)).digest()[-1] < 256*test_ratio
housing = load_housing_data()
housing_with_id = housing.reset_index()
housing_with_id["id"] = housing["longitude"]*1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

housing["income_cat"] = np.ceil(housing["median_income"]/1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace = True)

split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
	strat_train_set = housing.loc[train_index]
	strat_test_set = housing.loc[test_index]

for set_ in (strat_train_set, strat_test_set):
	set_.drop("income_cat", axis = 1, inplace = True)

housing = strat_train_set.copy()
corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))

housing.plot(kind = "scatter", x = "longitude", y = "latitude", alpha = 0.4,
			s = housing["population"]/100, label = "population", figsize = (10,7),
			c = "median_house_value", cmap = plt.get_cmap("jet"), colorbar = True)
plt.legend()



plt.show()
