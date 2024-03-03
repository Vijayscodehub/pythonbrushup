name = "Norwegian Blue"
# print(name)
# print(name[11])

#positive indexing

# print(name[3])
# print(name[4])
# print(name[9])
# print(name[3])
# print(name[6])
# print(name[8])
# print(name[-1])

# #negative indexing

# print(name[-11])
# print(name[-10])
# print(name[-5])
# print(name[-11])
# print(name[-8])
# print(name[-6])
# print()
# print(name[3-14])
# print(name[4-14])
# print(name[9-14])
# print(name[3-14])
# print(name[6-14])
# print(name[8-14])

# first = "we win"

# # def compare(a,b):
# #     for x in a:
# #         for y in b:
# #             if x ==y:
# #                 print(x)

# def compare(a,b):
#     for x in b:
#         if x in a:
#             print(x)
                
# compare(name,first)


# # #slicing
# print(name[0:6])
# print(name[3:5])
# print(name[0:9])
# print(name[:9])
# print(name[3:])
# print(name[:6])
# print(name[6:])
# print(name[:6]+ name[6:])
# print(name[:])

# #Norwegian BLue
# #01234567890123

# #Norwegian BLue
# #43210987654321 (-)
# #negative slicing
# # print(name[-4:-2])
# # print(name[-4:12])
# # print(name[-4:12])
# print(name[:-8])
# print(name[-11:-9])
# print(name[-14:-5])
# print(name[:-5])
# print(name[-11:])
# print(name[:-8])
# print(name[-8:])
# print(name[-8:]+name[:-8]) #-8 till end (ian blue) and start till -8 (Norweg)
# print(name[:-8]+name[-8:]) #-8 till end (ian blue) and start till -8 (Norweg)



# #Norwegian BLue
# #01234567890123

print(name[0:6:2])
print(name[0:6:3])
print(name[0::3])
print(name[::2])

number = "9,222;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

 