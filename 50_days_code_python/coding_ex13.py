def birth_year(year_of_birth,current_year=2023):
    age = current_year - year_of_birth
    return age


year_of_birth=int(input("what is your year_of_birth?  "))
age=birth_year(year_of_birth)
if age<=120:
    print(age)
else:
    print("Hold on there, grandpa! That's a bit overhead!")