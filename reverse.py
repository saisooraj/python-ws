num = int(input("enter the no:"))
tnum = num
rev = 0
while tnum != 0:
    rem = tnum%10
    rev=rev*10+rem
    tnum=tnum//10
   
print(rev)