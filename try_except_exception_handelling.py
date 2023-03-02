print("enter num1..")
num1=input()
print("enter num2..")
num2=input()
try:
   print("the sum of this two number is:",int(num1)+int(num2))
except Exception   as e:
    print(e)
    print("this line is very important")