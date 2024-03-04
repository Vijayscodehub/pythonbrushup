# print("Today, I am brushing up python 21/02/24... I'll be going from basics to oops to solving leetcode,hackerrank,codechef problems. but after completing oops i'll start c++ and do python problems sideby side then might also go for rust")
# print("Los gehts!")
# print("Hello"+"you")

# # name = input("Enter your name : ")

# # print("Hello"+" "+ name)

############ Variable and types ###################
time = 2
print(time)
print(type(time))

greeting = "hello"
print(greeting)
print(type(greeting))

# time= "2 'o clock "
# print(time)
# print(type(time))

# print(greeting + " " + time) #TypeError: can only concatenate str (not "int") to str


############# USE of Fstrings
val = 4
text = "here, "
print(text+f"Four in number is : {val}")  # using f string to concatenate str and int
print(f"Pi is approx {22/7:12.50f}")
pi = 22/7
print(f"Pi is approx {pi:12.50f}")  #12.50f is for precision