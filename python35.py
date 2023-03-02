# print a * pattarn
num = int(input("Enter no of rows which you want to print in the pattern: "))
num1 = input("Enter 1 for Normal or 0 for Reverse: ")
if num1 == "1":
    for i in range(num):
        for j in range(i+2):
            print("*",end=' ')
        print()
if num1 == "0":
    for i in range(num):
        for j in range(i,num):
            print("*", end=' ')
        print()