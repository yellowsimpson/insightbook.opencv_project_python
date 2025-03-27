import numpy as np

# 리스트를 numpy 배열로 변환
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

################################################################################################
# a = np.uint8([1,2,3,4])
# print(a)

# a = np.array([[1,2,3,4], [5, 6, 7, 8]])
# print(a)
# print(a.dtype)
# print(a.shape)

# b = np.array([[1,2,3,4], [5,6,7,8]])
# print(b)
# print(b.dtype)
# print(b.shape)

# c = np.array([1, 2, 3.14, 4])
# print(c)
# print(c.dtype)
# print(c.shape)

# d = np.array([1,2,3,4], dtype = np.flaot32)
# print(d)

# a = np.empty((2,3))
# print(a)

# a = np.array([[1,2,3,4], [5, 6, 7, 8]])
# a.fill(255)
# print(a)

# b = np.zeros((2,3))
# print(b)
# print(b.dtype)


a = np.empty_like(img)
b = np.zeros_like(img)
c = np.ones_like(img)
d = np.full_like(img, 255)

print(a)
print(b)
print(c)
print(d)

