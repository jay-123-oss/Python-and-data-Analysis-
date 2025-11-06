from tkinter import *

root = Tk()
root.minsize(999,555)

def check():
    status_var.set("successful")
    

haddiin = Label(root, text="Student form",font="cursiv 30 bold",justify=CENTER,padx=90)
haddiin.grid(row=0, column=2)

username = Label(root, text="username",font="cursiv 15 bold",)
username.grid(row=2,column=3)

password = Label(root, text="password",font="cursiv 15 bold")
password.grid(row=3,column=3)

email = Label(root, text="email",font="cursiv 15 bold")
email.grid(row=4,column=3)

date = Label(root, text="date of brith",font="cursiv 15 bold")
date.grid(row=5,column=3)

hobby = Label(root, text="Hobby",font="cursiv 15 bold")
hobby.grid(row=6,column=3)

uservalue = StringVar()
passvalue = StringVar()
emailvalue = StringVar()
datevalue = StringVar()
hobbyvalue = StringVar()
checkvalue = StringVar()

userentery = Entry(root, textvariable=uservalue)
userentery.grid(row=2,column=4)

passentery = Entry(root, textvariable=passvalue)
passentery.grid(row=3,column=4)

emailentery = Entry(root, textvariable=emailvalue)
emailentery.grid(row=4,column=4)

dateentery = Entry(root, textvariable=datevalue)
dateentery.grid(row=5,column=4)

hobbyentery = Entry(root, textvariable=hobbyvalue)
hobbyentery.grid(row=6,column=4)

button = Button(root,text="sumbite",font="normal 20 ",command=check)
button.grid(row=7,column=4)

#checkbutton 
checkbox = Checkbutton(text="what are yuo handicap?", textvariable=checkvalue)
checkbox.grid(row=8,column=3)



# ...existing code...
status_var = StringVar()
sl = Label(root, textvariable=status_var, text="")
sl.grid(row=9, column=6)


# ...existing code...


root.mainloop()