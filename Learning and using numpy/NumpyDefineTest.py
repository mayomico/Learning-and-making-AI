import numpy as np
#This is a learning file for me to use numpy.
#np.array(),this is an example.
print("----------define----------")
a=np.array([1,3,4,5])
d=np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Two dimension:\n",d)
#np.array can define a array in any dimensions
#Absolutaly some special arrays have their own formulation
b=np.eye(3,3)#The formula is to get an identity martix
print("identity martix:",b)
print("----------get information----------")
#they successfully define array in one and two dimension.Sure,you can define every dimension if you want to.
print("a size",a.size)#show how many elements in the array
print("a shape",a.shape)#show the size of each dimension,a is a one dimension array so output (4,)
print("d shape",d.shape)#the d is two dimension so output (3,3)
print("a nidm",a.ndim)#display the specific dimension (1 dimension)
print("d nidm",d.ndim)#(2 dimension)
print("a dtype",a.dtype)#show the types of elements in the array(element in a is 64int)
print("----------operation----------")
c=np.array([
    [2,4,6],
    [8,10,12]
])#we difine c to do some operations:
print("c and its transposition:\n",c,"\n\n",c.T)
print("add:",d+b)
print("multiply:",d@c.T,"\n\n",c@d)