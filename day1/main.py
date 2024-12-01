import numpy as np

data = np.loadtxt("input1.txt", dtype=int)
data = np.sort(data, axis=0)
result = np.abs(data[:, 1] - data[:, 0])
print( np.sum(result))

counts = np.array([np.sum(data[:,1] == num) for num in data[:,0]])
data = np.hstack((data, counts.reshape(-1, 1)))
print(np.sum(data[:,0] * data[:,2]))