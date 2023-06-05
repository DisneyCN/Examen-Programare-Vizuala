from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
# import pyperclip
# create function what will open file manager and user will choose txt file


   
root = Tk()
root.title('Editor de texte')
root.resizable(False, False)
root.geometry('400x400')

# Text editor
txt_edit = Text(root, height=24, bg="#32a852")
txt_edit.grid(column=0, row=0, sticky='nsew')



def OpenButton():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        print(text)
        txt_edit.insert(END, text)
    root.title(f"{filepath}")


def SaveButton():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    root.title(f" {filepath}")


def NewButton():
    with open("newFile.txt", "w") as output_file:
        txt_edit.delete(1.0, END)
    root.title(f"New file")

def CutButton():    
    pass
    # pyperclip.copy(txt_edit.get(1.0, END))
    # txt_edit.delete(1.0, END)

def CopyButton():
    pass

    # pyperclip.copy(txt_edit.get(1.0, END))

def PasteButton():
    pass
    # txt_edit.insert(END, pyperclip.paste())

def DeleteButton():
    txt_edit.delete(1.0, END)

def SelectAllButton():
    txt_edit.tag_add(SEL, 1.0, END)

def HelpButton():
    messagebox.showinfo("Help", "Cette application permet d'éditer des fichiers texte")

def AboutButton():
    messagebox.showinfo("Dezzvoltator", "Petcu Iuliana")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=NewButton)
filemenu.add_command(label="Open", command=OpenButton)
filemenu.add_command(label="Save", command=SaveButton)
filemenu.add_command(label="Save as...", command=SaveButton)
filemenu.add_command(label="Close", command=root.destroy)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Cut    CTRL + X", command=CutButton)
editmenu.add_command(label="Copy   CTRL + C", command=CopyButton)
editmenu.add_command(label="Paste  CTRL + V", command=PasteButton)
editmenu.add_command(label="Delete CTRL + Z", command=DeleteButton)
editmenu.add_command(label="Select All CTRL + A", command=SelectAllButton)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=HelpButton)
helpmenu.add_command(label="About...", command=AboutButton)
menubar.add_cascade(label="Help", menu=helpmenu)



root.config(menu=menubar)
root.mainloop()