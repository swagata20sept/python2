# build and import module and work with it.....
# from funcions import get_todos,write_todos
import funcions
import time

now=time.strftime("%b %d %Y %H:%M:%S")
print(now)

todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    if  user_action.startswith('add'):
            todo=user_action[4:]
            todos = funcions.get_todos()
            todos.append(todo + '\n')
            funcions.write_todos(todos)
    elif user_action.startswith('show'):
              todos = funcions.get_todos()
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
            todos = funcions.get_todos()
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
            funcions.write_todos(todos)
        except ValueError:
            print("invalid command...")
        continue

    elif user_action.startswith('complete'):
        try:
            number=int(input("number of the todo to complete"))
            todos = funcions.get_todos()
            index=number-1
            todo_to_remove=todos[index]
            todos.pop(index)
            funcions.write_todos(todos)
            messege=f"todos {todo_to_remove} was remove from the list..... "
        except IndexError:
            print("there is no item with this number...")
            continue
    elif  user_action.startswith('exit'):
            break
    else:
        print("command is not valid....")
print("bye!")