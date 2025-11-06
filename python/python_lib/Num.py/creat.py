import numpy as np
print("creat arrary")
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

print("creat multy-daimention arrary")
arr1  =np.array([[1,2,3,7],[4,5,6,5]])
print(arr1)


print("zeros arrary ")
print(np.zeros((3,3)))
print(np.zeros((3,)))
print(np.zeros((2,3)))
print(np.zeros((2,2)))

print("ones arrayr ")
print(np.ones((3,3)))
print(np.ones((3,)))
print(np.ones((2,3)))
print(np.ones((2,2)))


print("arnge arrayr ")
print(np.arange(1,20,2))


print("line space ")
print(np.linspace(0,1,5)) #0 se 1 ke beech 5 part equal part 


print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)
print(arr1.size)


