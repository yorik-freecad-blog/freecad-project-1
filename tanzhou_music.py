#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import urllib
import json

def music():
	if not entry.get():
		tkMessageBox.showinfo("wenjing tixi:", "content not blank")
		return
	name=entry.get()
	html=urllib.urlopen("http://s.music.163.com/search/get/?type=1&s=%s&limit=9"%name).read()
	js=json.loads(html)
	print(html)
	for i in js['result']['songs']:
		print(i)

root=Tk()
root.title("tazhou music")
root.geometry("+700+200")
entry=Entry(root)
entry.pack()
button=Button(root, text="search", command="music", fg="blue")
button.pack()
listbox=Listbox(root)
listbox.pack()
label=Label(root, text="tanzhou music", fg="red")
label.pack()
root.mainloop()