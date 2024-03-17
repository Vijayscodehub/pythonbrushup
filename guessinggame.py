answer = 5

print("Please guess number btw 1 - 10")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it!")
#     else:
#         print("You did not guess it corrently fucker")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it!")
#     else:
#         print("You did not guess it corrently fucker")
# else:
#     print("your guess is correct !")

if guess == answer:
     print("You guessed it in first time")
else:
    if guess < answer:
        print("Please guess higher")
    else: 
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You guessed it correct")
    else: 
        print("You are incorrent, rerun the code")
   
        
    