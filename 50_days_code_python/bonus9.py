# create a strong password using a list...
password=input("enter new password: ")
result=[]
if len(password)>=8:
    result.append(True)
else:
    result.append(False)
digit=False
for i in password:
    if i.isdigit():
        digit=True
        result.append(digit)
uppercase=False
for i in password:
    if i.isupper():
                uppercase=True
                result.append(uppercase)
                print(result)
if all(result):
    print("strong password...")                
else:
    print("weak password...")
