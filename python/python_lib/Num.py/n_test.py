import numpy as np

# # arr=np.arange(1,20,2)
# # drr = np.arange(1,40,4)
# # arrr = np.array(arr,drr)
# # print(arrr)

# # arr=np.linspace(0,20,20).astype("int")
# # print(arr)

# arr = np.eye(3,3)
# print(arr)

# arr=np.random.rand(10)
# print(arr)

# arr1=np.random.randint(1,3)
# print(arr1)


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,3,3],[5,5,6],[6,8,9]])

print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))



