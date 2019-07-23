P = int(input("enter the points: "))
if( P>0 and P<1000 ):
    print("silver card member")
elif (P>1000 and P<=10000):
     print("gold card member")
else:
    print("platinum card members")
