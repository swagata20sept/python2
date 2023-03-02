# Write a program that asks users to enter a password. Then, it checks if the password length is greater than 7 and returns "Great password there!".
# If the password has 7 or fewer characters, the program returns, "Your password is weak".
#password=input("enter a password: ")
# if len(password)>7:
 #   print("Great password there!")
# else:
 #   print("Your password is weak")
 
 #Extend the program we built in Coding Exercise 1 by adding a new feature. The new feature should allow the program to return "Password is OK, but not too strong" when the password is exactly seven characters long.
password=input("enter a password: ")
if len(password)>7:
    print("Great password there!")
elif len(password)==7:
    print("Your password is weak")
else:
    print("Password is OK, but not too strong")
