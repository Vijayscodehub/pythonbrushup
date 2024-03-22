val = int(input("what's your score "))
## when comparing conditions with and , python will stop as soon as it finds a condition which is False

#and->false

# # if val >= 35 and val<=100:
# if 35<=val<=100:
#     print("Great,You Passed ! with score:{}" .format(val))
# else:
#     print("You Failed, with score: {}".format(val))
# print("-"*58)

## OR 
#when comparing conditions with or , python will stop as soon as it finds a condition which is True
if val < 35 or val > 100:
    print("You Failed, with score: {}".format(val))
    
else:
    print("Great,You Passed ! with score:{}" .format(val))
print("-"*58)
#simpllfied chained comparison    
