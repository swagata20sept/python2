todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("enter a todo: ")+"\n"
            file=open('todos.txt','r')
            todos=file.readlines()
            file.close()
            todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
             file=open('todos.txt','r')
             todos=file.readlines()
             file.close()
             for index,item in enumerate(todos):
                item=item.strip('\n')
                row=f"{index+1}-{item}"
                print(row)
                #print("hello",index,item)
                print(f"length is {index+1}")
        case 'edit':
            number=int(input("the number of todo to edit: "))
            number=number-1
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
        case 'complete':
            number=int(input("number of the todo to complete"))
            todos.pop(number)
        case 'exit':
            break
print("bye!")