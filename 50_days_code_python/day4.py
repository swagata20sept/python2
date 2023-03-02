todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
             print(item)
        case 'edit':
            number=int(input("the number of todo to edit: "))
            number=number-1
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
        case 'exit':
            break
print("bye!")