num = int(input("enter the no :"))
res = 0
while num!=0:
    res += ((num%10) ** 3)
    num=num//10
if num==res:
    print("the no is amstrong:")
else:
    print("the no is not an amstrong:")