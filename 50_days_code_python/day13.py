# default argument.....
def get_todos(filepath='todos.txt'):
      with open(filepath,'r') as file:
              todos=file.readlines()
              return todos


def write_todos(todos_arg,filepath='todos.txt'):
    with open(filepath,'w') as file:
             file.writelines(todos_arg)


todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    if  user_action.startswith('add'):
            todo=user_action[4:]
            todos = get_todos()
            todos.append(todo + '\n')
            write_todos(todos)
    elif user_action.startswith('show'):
              todos = get_todos()
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
            todos = get_todos()
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
            write_todos(todos)
        except ValueError:
            print("invalid command...")
        continue

    elif user_action.startswith('complete'):
        try:
            number=int(input("number of the todo to complete"))
            todos = get_todos()
            index=number-1
            todo_to_remove=todos[index]
            todos.pop(index)
            write_todos(todos)
            messege=f"todos {todo_to_remove} was remove from the list..... "
        except IndexError:
            print("there is no item with this number...")
            continue
    elif  user_action.startswith('exit'):
            break
    else:
        print("command is not valid....")
print("bye!")