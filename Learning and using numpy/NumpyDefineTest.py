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
b=np.eye(3,3,0,int)#The formula is to get an identity martix
#np.eye(row shape,column shape,offset,type)
print("identity martix:\n",b)
print("identity martix but has a offset:\n",np.eye(3,3,1,int))
#np.zero can be used to create a null matrix
zero=np.zeros((3,3),int)
print("zeros matrix:\n",zero)
#np.ones can be used to create a unit matrix
one=np.ones((3,3),int)
print("ones matrix:\n",one)
#np.arange can define a matrix like "for i in range()" and it can choose a specific type of values
arange=np.arange(1,100,5,int)
print("arange matrix:\n",arange)
#np.linspace is always stronger than np.arange because you just need set a start and a stop,system can get its gap automatically
linspace=np.linspace(1,13,23,True,False,float)
print("linspace matrix:\n",linspace)
print("----------get information----------")
#they successfully define array in one and two dimension.Sure,you can define every dimension if you want to.
print("a size",a.size)#show how many elements in the array
print("a shape",a.shape)#show the size of each dimension,a is a one dimension array so output (4,)
print("d shape",d.shape)#the d is two dimension and each has 3 numbers so output (3,3)
print("a nidm",a.ndim)#display the specific dimension (1 dimension)
print("d nidm",d.ndim)#(2 dimension)
print("a dtype",a.dtype)#show the types of elements in the array(element in a is 64int)
print("----------operation----------")
c=np.array([
    [2,4,6],
    [8,10,12]
])#we difine c to do some operations:
print("c and its transposition:\n",c,"\n\n",c.T)
#ATTENTION:even two matrixs have different shape,it still can suceeed
print("plus:\n",d+b)
print("multiply(matrix multiple):\n",d@c.T,"\n\n",c@d)
print("minus\n",d-b)
#these formulas is for all of vlaue in the matrix
print("sum\n",np.sum(d))
print("max\n",np.max(d))
print("min\n",np.min(d))
print("mean\n",np.mean(d))
