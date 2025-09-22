import numpy as np

A = np.array([[9,8],[7,4]])
print(A)

B = np.array([[6,5],[7,9]])
print(B)

add = A+B
print(add)

mul = A*B
print(mul)

result = np.dot(A, B)
print(result)