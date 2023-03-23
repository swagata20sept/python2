# file compresser..............................
import PySimpleGUI as sg
from zip_creater import make_archive
lable1=sg.Text("select file to compress:")
input1=sg.Input()
choose_button1=sg.FileBrowse("choose",key="files")
lable2=sg.Text("select destination folder:")
input2=sg.Input()
choose_button2=sg.FilesBrowse("choose")
compress_button=sg.FolderBrowse("compress",key="folder")
output_lable=sg.Text(key="output")
window=sg.Window("file compresser",layout=[[lable1,input1,choose_button1],[lable2,input2,choose_button2],[compress_button,output_lable]])

while True:
    event,values=window.read()
    print(event,values)
    filepaths=values["files"].split(";")
    folder=values['folder']
    make_archive(filepaths,folder)
    window["output"].update(value="compression completed!")
window.close