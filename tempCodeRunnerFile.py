    # print("Value of : {0} squared is {1} and cubed is {2}".format(x, x**2,x**3))
    

# n = int(input())
# y = ""
# for x in range(1,n+1):
#     z = str(x)
#     y = y+z
    
# print(y)


n = int(input())
arr = map(int, input().split())
# y = 0
# L = []
# for x in arr:
#     if x > y:
#         y = x
#         L.append(x)
# z= len(L)
# print(L[-1])
L= []
y = 0
for x in arr:
    if not x in L:
        L.append(x)
L.sort()
print(L)
print(L[-2])