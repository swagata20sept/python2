import funcions
import PySimpleGUI as sg
lable= sg.Text("type in a To-Do : ")
input_box=sg.InputText(tooltip="enter to-do")
add_button= sg.Button("Add")
window=sg.Window('my to-do app',layout=[[lable],[input_box,add_button]])
window.read()
window.close()
