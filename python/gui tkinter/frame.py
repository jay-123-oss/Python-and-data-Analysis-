from tkinter import *

root = Tk()
root.minsize(1200,900)

f1 = Frame(root, bg="black", borderwidth=5,relief="groove" )
f1.pack(side=LEFT, fill="y")
l_f1 = Label(f1, text="hello",fg="red" ,font=15)
l_f1.pack()

f2 = Frame(root, bg="black",borderwidth=5, relief="ridge")
f2.pack(side=TOP, fill="x")
l_f2 = Label(f2, fg="red", font=15, text="wellcome to tkinter ",  )
l_f2.pack()

root.mainloop()