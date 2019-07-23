m1 = int(input("enter the marks for subject 1: "))
m2 = int(input("enter the marks for subject 2: "))
m3 = int(input("enter the marks for subject 3: "))
if(m1>35 and m2>35 and m3>35):
    avg=(m1+m2+m3)/3
    if(avg>35 and avg<65):
        print("C grade")
    elif(avg>66 and avg<85):
        print("B grade")
    elif(avg>86 and avg<100):
        print("A grade")
    else:
            print("something really went wrong")

else:
    print("better luck next time!")
