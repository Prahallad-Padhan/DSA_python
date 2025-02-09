import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.reshape(a,(3,3))
print(m)

m = np.append(m,[[10,11,12]],0)
print(m)

m = np.delete(m,[3],0)
print(m)