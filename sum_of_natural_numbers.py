'''program to find sum of first 'n' natural numbers'''
n = int(input("enter the no:"))
res=0
for ele in range(1,n+1):
    res += ele
print(f"sum of first {n} natural number is : {res}")