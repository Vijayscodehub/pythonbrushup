age = 24
# print("My age is " + str(age))  #int conv to str for concatenation

#Using replacement fields
print("My age is {0} " .format(age))  #no need to chnage type

print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}"
      .format(31,"Jan","mar","May","Jul","Aug","oct","Dec"))

print("Jan:{2},Feb:{0},Mar:{2},Apr:{1} ".format(28,30,31))

print("""Jan:{2}
Feb:{0}
Mar:{2}
Apr:{1} """.format(28,30,31))
