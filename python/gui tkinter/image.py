
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.minsize(900,888)
# png image for 
'''
j_img = PhotoImage(file="j.png")
j_label = Label(image=j_img)
j_label.pack()
#png end 
'''
# for jpg images 
j_image = Image.open("J.jpg")
photo = ImageTk.PhotoImage(j_image)
j_label = Label( root, image=photo)
j_label.pack()
#eng jpg
root.mainloop()


