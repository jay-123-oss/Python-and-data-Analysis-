import tkinter as tk
from tkinter import scrolledtext

# ----------------- Window -----------------
window = tk.Tk()
window.title("Mini Chat App")
window.geometry("400x500")

# ----------------- Chat Display -----------------
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.pack(pady=10)

# ----------------- Message Entry -----------------
msg_entry = tk.Entry(window, width=30, font=("Arial", 14))
msg_entry.pack(side=tk.LEFT, padx=10, pady=10)

# ----------------- Send Function -----------------
def send_message():
    msg = msg_entry.get()
    if msg.strip() != "":
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "You: " + msg + "\n")
        chat_area.insert(tk.END, "Bot: " + f"Echo: {msg}\n")  # Simple echo bot
        chat_area.yview(tk.END)
        chat_area.config(state='disabled')
        msg_entry.delete(0, tk.END)

# ----------------- Send Button -----------------
send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, pady=10)

# ----------------- Enter Key Binding -----------------
window.bind('<Return>', lambda event: send_message())

window.mainloop()
