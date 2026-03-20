import numpy as np


a=np.array([10,20,30,40,50])
b=np.array([11,22,33,44,55])

# print(type(a))
c= a+b
print("Add :",c)

c= a-b
print("Sub :",c)

c= a*b
print("Mul :",c)

c= a/b
print("Div :",c)

c= b%a
print("Modulus :",c)

print(np.max(a))
print(np.min(b))