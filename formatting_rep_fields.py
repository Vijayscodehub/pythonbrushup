# for x in range(1,14):
#     # print("Value of : {0} squared is {1} and cubed is {2}".format(x, x**2,x**3))
    
#     # print("Value of : {0:2} squared is {1:3} and cubed is {2:4}".format(x, x**2,x**3))
    
#     # print("Value of : {0:2} squared is {1:<3} and cubed is {2:<4}".format(x, x**2,x**3))  #< left align, > right align
    
#     print("Value of : {0:2} squared is {1:<3} and cubed is {2:^4}".format(x, x**2,x**3))  #< left align, > right align, ^ center align
    
    #max precision of python floating point number is btw 52 and 53
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

for x in range(1,14):
    print("Value of : {} squared is {} and cubed is {:4}".format(x, x**2,x**3))