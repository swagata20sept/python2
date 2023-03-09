import PySimpleGUI as sg

lable1= sg.Text("select filee to compress:")
input1=sg.Input()
choose_button1=sg.FileBrowse("choose")
lable2=sg.Text("select destination folder:")
input2=sg.Input()
choose_button2=sg.FileBrowse("choose")
compress_button=sg.Button("compress")
window=sg.Window("file compressor",layout=[[lable1,input1,choose_button1],[lable2,input2,choose_button2],[compress_button]])
window.read()
window.close()