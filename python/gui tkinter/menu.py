from tkinter import *

root =Tk()
root.minsize(731,531)
root.title("this is menu classes")

def myfunc():
    print("hello")

menubar = Menu(root)
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_separator()
m1.add_command(label="print",command=myfunc)
m1.add_command(label="add",command=myfunc)
m1.add_command(label="new",command=myfunc)
m1.add_separator()
m1.add_command(label="folder",command=myfunc)

menubar.add_cascade(label="file",menu=m1)

# for edit
m2 = Menu(menubar, tearoff=0)
m2.add_command(label="copy",command=myfunc)
m2.add_command(label="pest",command=myfunc)
m2.add_separator()
m2.add_command(label="remove",command=myfunc)
m2.add_command(label="delete",command=myfunc)
m2.add_command(label="mark",command=myfunc)
m2.add_separator()
m2.add_command(label="other",command=myfunc)

menubar.add_cascade(label="edit",menu=m2)





root.config(menu=menubar)
root.mainloop()
