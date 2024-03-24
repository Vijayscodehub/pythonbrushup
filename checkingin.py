song = "Another Love"

letter = input("Please enter a letter : ")

if letter in song:
    print("Letter %s is there in song" %(letter))  #its case sensitive
if letter not in song:
    print("Its not there")
    
