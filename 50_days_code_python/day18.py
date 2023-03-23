import funcions
import PySimpleGUI as sg
import time
import os
if not os.path.exists("todos.txt"):
       with open("todos.txt",'w') as file:
              pass

sg.theme("darkPurple")
clock=sg.Text('',key='clock')
lable= sg.Text("type in a To-Do : ")
input_box=sg.InputText(tooltip="enter to-do", key="todo")
add_button= sg.Button("Add")
list_box=sg.Listbox(values=funcions.get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("complete")
exit_button=sg.Button("Exit")
window=sg.Window('my to-do app',layout=[[clock],[lable],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]])

while True:
           event,values=window.read(timeout=20000000)
           window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
           print(1,event)
           print(2,values)
           print(3,values['todos'])
           match event:
                   case "Add":
                           todos=funcions.get_todos()
                           new_todo=values['todo']+"\n"
                           todos.append(new_todo)
                           funcions.write_todos(todos)
                   case "Edit":
                        try:
                            todo_to_edit=values['todos'][0]
                            new_todo=values['todo']
                            todos=funcions.get_todos()
                            index=todos.index(todo_to_edit)
                            todos[index]=new_todo
                            funcions.write_todos(todos)
                            window['todos'].update(values=todos)
                        except IndexError:
                               sg.popup("please select an item first...",font=("Helvetica",20))
                   case "complete":
                           todo_to_complete=values['todos'][0]
                           todos=funcions.get_todos()
                           todos.remove(todo_to_complete)
                           funcions.write_todos(todos)
                           window['todos'].update(values=todos)
                           window['todo'].update(value='')
                   case "Exit":
                           break
                   case "todos":
                           window['todo'].update(value=values['todos'][0])
                   case sg.WIN_CLOSED:
                     break 
window.close()