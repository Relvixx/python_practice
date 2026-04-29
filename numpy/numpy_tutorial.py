import numpy as np

"""myarr = np.array([[1,2,3,4,5]], np.int32)
print(myarr)
print(type(myarr))
print(myarr.shape)
print(myarr.dtype)"""

'''myarr[0,4] = 50
print(myarr)
arr=np.arange(0,50)
print(arr)
lspace = np.linspace(0,50)
print(lspace)'''

l = [[1,2,3], [4,5,6], [7,8,9]]
ar = np.array(l)
print(ar)
print(ar.T)
print(ar.sum(axis=0))
print(ar.sum(axis=1))