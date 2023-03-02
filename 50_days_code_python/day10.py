# error handaling..
todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    if  user_action.startswith('add'):
            todo=user_action[4:]
            with open('todos.txt','r') as file:
              todos=file.readlines()
            todos.append(todo + '\n')
            with open('todos.txt','w') as file:
             file.writelines(todos)
    elif user_action.startswith('show'):
             with open('todos.txt','r') as file:
              todos=file.readlines()
              for index,item in enumerate(todos):
                item=item.strip('\n')
                row=f"{index+1}-{item}"
                print(row)
                #print("hello",index,item)
                print(f"length is {index+1}")
    elif user_action.startswith('edit'):
        
        try:
            number=int(input("the number of todo to edit: "))
            number=number-1
            with open('todos.txt','r') as file:
              todos=file.readlines()
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
            with open('todos.txt','w') as file:
             file.writelines(todos)
        except ValueError:
            print("invalid command...")
        continue

    elif user_action.startswith('complete'):
        try:
            number=int(input("number of the todo to complete"))
            with open('todos.txt','r') as file:
              todos=file.readlines()
              index=number-1
              todo_to_remove=todos[index]
            todos.pop(index)
            with open('todos.txt','w') as file:
             file.writelines(todos)
             messege=f"todos {todo_to_remove} was remove from the list..... "
        except IndexError:
            print("there is no item with this number...")
            continue
    elif  user_action.startswith('exit'):
            break
    else:
        print("command is not valid....")
print("bye!")