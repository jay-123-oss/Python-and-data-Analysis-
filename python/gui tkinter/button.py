from tkinter import*
root= Tk()
root.title("button")
Frame = Frame(root, bg="red",border=5,relief="solid",borderwidth=6)
Frame.pack(side=TOP,anchor="nw",fill=X)

def hello():
    print("hello, wellcome to our tkinter program.")


b1 = Button(Frame, bg="white", padx=20,border=5, command=hello,text="btn")
b1.pack(side=LEFT,fill="x",padx=30)

b2 = Button(Frame, bg="white", padx=20,border=5, command=hello,text="btn")
b2.pack(side=LEFT,fill="x",padx=30)

b3 = Button(Frame, bg="white", padx=20,border=5, command=hello,text="btn")
b3.pack(side=LEFT,fill="x",padx=30)

b4 = Button(Frame, bg="white", padx=20,border=5, command=hello,text="btn")
b4.pack(side=LEFT,fill="x",padx=30)

b5 = Button(Frame, bg="white", padx=20,border=5, command=hello,text="btn")
b5.pack(side=LEFT,fill="x",padx=30)

root.mainloop()