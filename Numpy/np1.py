a=[10,20,30,40,50]
b=[11,22,33,44,55]



# c= []
# for i in range(len(a)):
#     c.append(a[i]+b[i])

    
    
c=[a[i]+b[i] for i in range(len(a))]
print(c)
