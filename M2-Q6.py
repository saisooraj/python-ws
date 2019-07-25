import functools
lis = [1,2,3,4,5,6,7,8,9]
print ("The sum of the list elements is : ") 
print (functools.reduce(lambda a,b : a+b,lis)) 