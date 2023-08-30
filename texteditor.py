from tkinter import *
from tkinter import filedialog
from tkinter import font

root= Tk()
root.title('Text editor in python')
root.iconbitmap('C:\\Users\\KIIT\\Desktop\\image')
root.geometry('1200x660')

#create new file
def new_file():
    my_text.delete("1.0", END)
    root.title('New file-texteditor')
    status_bar.config(text="New file    ")

def open_file():
    my_text.delete("1.0", END)

    text_file= filedialog.askopenfilename(title="Open file", filetypes=(("Text files", "*.txt"), ("HTML Files", ".*html"), ("Python files", ".*py"), ("All Files", "*.*")))
    name= text_file
    status_bar.config(text=f'{name}        ')
    name=name.replace("C:\\Users\\KIIT\\Desktop\\text editor in python","")
    root.title(f'{name} -Textpad!')

    #open the file
    text_file= open(text_file, 'r')
    stuff= text_file.read()
    #add file to textbox
    my_text.insert(END, stuff)
    #close the opened file
    text_file.close()


    #create save_as_file
    #create save_as_file
def save_as_file():
        text_file= filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:\\Users\\KIIT\\Desktop\\text editor in python", title="Save File", filetypes=(("Text Files", "*.txt"), ("Html files", "*.html"), ("Python Files", "*.py"), ("All files", "*.*")))
        if text_file:
            name=text_file
            status_bar.config(text=f'{name}        ')
            name= name.replace("C:\\Users\\KIIT\\Desktop\\text editor in python", "")
            root.title(f'{name} - Textpad!')

            #save the file
            text_file= open(text_file, "w")
            text_file.write(my_text.get(1.0, END))

            text_file.close()

   
#main frame
my_Frame= Frame(root)
my_Frame.pack(pady=5)
#create scrollbar
text_scroll= Scrollbar(my_Frame)
text_scroll.pack(side=RIGHT, fill=Y)
#create text box
my_text=Text(my_Frame, width=97, height=25, font= ("Helvetica", 16), selectbackground="black", undo=True, yscrollcommand= text_scroll.set)
my_text.pack()

#CONFIGURE
text_scroll.config(command=my_text.yview)
#create menu
my_menu= Menu(root)
root.config(menu=my_menu)
#add file menu
file_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command= new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#add edit menu
edit_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#add  view menu
view_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom")

#add status bar
status_bar= Label(root, text='Ready        ')
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()
