from tkinter import *
from tkinter import ttk
import requests

# ------------------- Functions -------------------
def get_weather():
    
    city = com.get()
    api_key = "b95a8322266cff6f78334ffc4ae0f5eb"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()
        if data.get("cod") == 200:
            w_label_1.config(text=data["weather"][0]["main"])
            wd_label_1.config(text=data["weather"][0]["description"].title())
            tem_label_1.config(text=f"{data['main']['temp']} °C")
            per_label_1.config(text=f"{data['main']['pressure']} hPa")
        else:
            w_label_1.config(text="City Not Found")
            wd_label_1.config(text="")
            tem_label_1.config(text="")
            per_label_1.config(text="")
    except Exception as e:
        w_label_1.config(text="Error")
        wd_label_1.config(text=str(e))
        tem_label_1.config(text="")
        per_label_1.config(text="")

# ------------------- GUI -------------------
root = Tk()
root.title("🌤 Modern Weather App")
root.geometry("500x600")
root.config(bg="#f0f4f7")
root.resizable(False, False)

# Header with gradient-like effect
header = Frame(root, bg="#00c6ff")
header.place(x=0, y=0, width=500, height=100)
title = Label(header, text="🌍 Weather App", font=("Helvetica", 26, "bold"), bg="#00c6ff", fg="white")
title.place(relx=0.5, rely=0.5, anchor=CENTER)

# Combobox (editable)
list_name = ["Bhopal", "Indore", "Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore", "Hyderabad", "Pune"]
com = ttk.Combobox(root, font=("Helvetica", 14), values=list_name, justify="center")
com.place(x=50, y=130, width=400, height=35)
com.set("")
com.config(state="normal")  # Editable

# Get Weather button (rounded with shadow effect)
btn = Button(root, text="🔍 Get Weather", font=("Helvetica", 14, "bold"), bg="#00bcd4", fg="white",
             activebackground="#0097a7", activeforeground="white", relief="flat", command=get_weather)
btn.place(x=150, y=180, width=200, height=45)

# Weather info display frame
info_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
info_frame.place(x=25, y=250, width=450, height=200)

w_label = Label(info_frame, text="Weather:", font=("Helvetica", 14, "bold"), bg="white")
w_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
w_label_1 = Label(info_frame, text="", font=("Helvetica", 14), bg="white", fg="#333")
w_label_1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

wd_label = Label(info_frame, text="Description:", font=("Helvetica", 14, "bold"), bg="white")
wd_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
wd_label_1 = Label(info_frame, text="", font=("Helvetica", 14), bg="white", fg="#333")
wd_label_1.grid(row=1, column=1, padx=10, pady=10, sticky=W)

tem_label = Label(info_frame, text="Temperature:", font=("Helvetica", 14, "bold"), bg="white")
tem_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
tem_label_1 = Label(info_frame, text="", font=("Helvetica", 14), bg="white", fg="#333")
tem_label_1.grid(row=2, column=1, padx=10, pady=10, sticky=W)

per_label = Label(info_frame, text="Pressure:", font=("Helvetica", 14, "bold"), bg="white")
per_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
per_label_1 = Label(info_frame, text="", font=("Helvetica", 14), bg="white", fg="#333")
per_label_1.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# Footer
footer = Label(root, text="Developed by Jaaydeep 🌟", font=("Helvetica", 10, "italic"), bg="#f0f4f7", fg="#555")
footer.place(relx=0.5, y=570, anchor=CENTER)

root.mainloop()
