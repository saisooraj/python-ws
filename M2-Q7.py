from functools import reduce
lis = [1,2,3,4,5,6,7,8,9]
even = []
lis2 = []
lis2 = list(filter(lambda x:x % 2 == 0,lis))
even = list(map(lambda x:x*x,lis2))
print(even)