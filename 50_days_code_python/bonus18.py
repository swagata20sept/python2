import PySimpleGUI as sg
from zip_creater1 import extract_archive
sg.theme("black")
leble1=sg.Text("select archive: ")
input1=sg.Input()
choose_button1=sg.FileBrowse("choose",key="archive")

leble2=sg.Text("select dest dir: ")
input2=sg.Input()
choose_button2=sg.FileBrowse("choose",key="folder")

extract_button=sg.Button("Extract")
output_leble=sg.Text(key="output",text_color="green")
window=sg.Window("Archive Extractor",layout=[[leble1,input1,choose_button1],[leble2,input2,choose_button2],[extract_button,output_leble]])
while True:
   event,values=window.read()
   print(event,values)
   archivepath=values["archive"]
   dest_dir=values["folder"]
   extract_archive(archivepath,dest_dir)
   window["output"].update(value="extraction completed.....")
window.close()