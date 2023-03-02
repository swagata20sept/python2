#prompt=input("the countries usa,india, germany .....enter the country name :  ")
#if prompt=='usa':
#    print("hello")
#elif prompt=='india':
 #   print("namaste")
#elif prompt=='germany':
 #   print("hola")
#else:
 #   print("i am not from this country")
 #...............................................................................................
#country = input("Where do you come from? ")
#match country:
 #   case 'USA':
  #      print('Hello')
   # case 'India':
    #    print('Namaste')
    #case 'Germany':
     #   print('Hallo')
     #..............................................................................................
#ingredients = ["john smith", "sen plakay", "dora ngacely"]
#for item in ingredients:
    #item=item.title()
 #   print(item.title())
 #..................................................................................................
 # to do list view and program exit# match case.........
"""
todos=[]
while True:
    user_action=input("type add,show or exit: ")
    match user_action:
        case 'add':
            todo=input("enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print("bye!")

"""
#.................................................................................
# improving the program output using for loop
todos=[]
while True:
    user_action=input("type add,show or exit: ")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
             print(item)
        case 'exit':
            break
print("bye!")