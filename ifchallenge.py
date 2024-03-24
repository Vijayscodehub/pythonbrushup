name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))

if 18<=age<31:
    print("Welcome to the Holiday,{1}, while your age is {0} and its btw 18-30" .format(age,name))
else:
    print("Sorry you don't fit in the crowd, %s" %(name))
