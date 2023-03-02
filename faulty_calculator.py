def calculator():
    print("welcome to your calculator...")
    oparation=input("please type in the math oparation you would like to complete:\n+ for addition\n-for substraction\n* for multiplication\n/ for division\n** for power\n% for modulo\nenter your choise:")
    num1=int(input("enter your first number:"))
    num2=int(input("enter your second number:"))
    if oparation=='+':
                    if num1==56 and num2==9:
                           print("56+9=77")
                    else:
                           print(f"{num1}+{num2}= {num1+num2}")
    elif oparation=='-':
                    print(f"{num1}-{num2}={num1-num2}")
    elif oparation=='*':
                    if num1==45 and num2==3:
                       print("45*3=555")
                    else:
                       print(f"{num1}*{num2}={num1*num2}")
    elif oparation=='/':
                    if num1==56 and num2==6:
                      print("56/6=4")
                    else:
                       print(f"{num1}/{num2}={num1/num2}")
    elif oparation=='**':
                    print(f"{num1}**{num2}={num1**num2}")
    elif oparation=='%':
                    print(f"{num1}%{num2}={num1%num2}")
    else:
                    print("you press a invalid key")
calculator()    