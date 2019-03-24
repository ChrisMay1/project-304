from __future__ import division
import numpy as np
import os

fname = os.path.join('datasets','housing','housing.csv')

def split_train_test(data, test_ratio):
	np.random.seed(42)
	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data)*test_ratio)
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return train_indices, test_indices

try:
	data = np.loadtxt(fname,delimiter = ',', dtype = 'str')
	hdrs, index = {}, 0
except IOerror:
	traceback.format_exc()

for hdr in data[0,:]:
	hdrs.update({hdr:index})
	index += 1
train_set, test_set = split_train_test(data, 0.2)

