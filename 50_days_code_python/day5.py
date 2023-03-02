todos=[]
while True:
    user_action=input("type add,show,edit or exit: ")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("enter a todo: ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
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
#...ex1:
#filenames = ['document', 'report', 'presentation']
#for index,item in enumerate(filenames):
 #   row=f"{index}-{item}.txt"
  #  print(row)
#...ex2:
#ips = ['100.122.133.105', '100.122.133.111']
#number=int(input("enter the index of the ip you want: "))
#print(f"you chose {ips[number]}")