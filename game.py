import random as random
num = rn.randint(1,6)
count = 0
while True:
    inp_num = int(input("enter the number: "))

    if inp_num == num:
        count += 1
        print(f"You generated number in {count} attempts ")
        break
    elif inp_num < num:
        print("Guessed number is less than actual number: ")
        count += 1
    else:
        print("Guessed number is more than the avtual number: ")
        count += 1
    if count == 3:
        print("Better luck next time")
        break
