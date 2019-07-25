name = input("Enter your name\n")
lst = ['a','e','i','o','u']
print(len(list(filter(lambda x: x in lst, name))))
