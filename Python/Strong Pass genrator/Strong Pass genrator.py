from random import choice

x = int(input("Enter lenght of your password : "))

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
         '*', '(', ')']

mypass = ""
for i in range(x) :
    mypass = mypass + choice(password)
print("Your Password is :  ",mypass)
