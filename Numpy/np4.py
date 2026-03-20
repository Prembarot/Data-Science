# 

import numpy as np

a=np.array([10,20,-40,-50,45,67,88,34,-2,-5,-7,-8])
# print(a)

# b=a>0
# print(b)
b=a[a>0]
print(b)

b=a[a<0]
print(b)

b=a[a>20]
print(b)

b=a[a%2==0]
print(b)

b=a[a%2==1]
print(b)