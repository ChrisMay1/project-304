from __future__ import division
import numpy as np
import os
import tarfile
from six.moves import urllib

download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_path = os.path.join("datasets","housing")
HOUSING_url = download_root + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url = HOUSING_url, housing_path = HOUSING_path):
	if not os.path.isdir(housing_path):
		os.makedirs(housing_path)
	tgz_path = os.path.join(housing_path, "housing.tgz")
	urllib.request.urlretrieve(housing_url, tgz_path)
	housing_tgz = tarfile.open(tgz_path)
	housing_tgz.extractall(path = housing_path)
	housing_tgz.clos(),
fetch_housing_data()

