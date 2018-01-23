from __future__ import division
import numpy as np
def func(x,y):
    return x/y

def test_answer():
	arr1 = np.array([2])
	arr2 = np.array([8])
	assert func(arr1,arr2) == 0.25
