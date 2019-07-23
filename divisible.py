n = int(input("enter the no :"))
c=0
i=1
while True:
    if(i%3==0 and i%6==0 and not i%9==0):
        print(i,end=" ") 
        c += 1
    if c == n:
        break
    i += 1