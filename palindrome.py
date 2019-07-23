num = int(input("enter the no:"))
tnum = num
rev = 0
while tnum != 0:
    rem = tnum%10
    tnum=tnum//10
    rev=rem*10+rem
if num==rev:
   print("palindrome")
else:
    print("not palindrome")