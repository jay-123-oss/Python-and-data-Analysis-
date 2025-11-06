import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime

# ================== Database Setup ==================
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    isbn TEXT,
    genre TEXT,
    quantity INTEGER
)
""")
conn.commit()

# ================== Login & Signup ==================
def signup():
    user = entry_su_user.get()
    pwd = entry_su_pass.get()
    if user == "" or pwd == "":
        messagebox.showerror("Error", "Username and password required!")
        return
    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (?,?)", (user,pwd))
        conn.commit()
        messagebox.showinfo("Success", "Signup successful! You can login now.")
        signup_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
    result = cursor.fetchone()
    if result:
        login_window.destroy()     # Close login window
        main_gui(user)             # Open main GUI
    else:
        messagebox.showerror("Error", "Invalid username or password")

def open_signup():
    global signup_window, entry_su_user, entry_su_pass
    signup_window = tk.Toplevel()
    signup_window.title("Signup")
    signup_window.geometry("350x200")
    tk.Label(signup_window, text="Username:").pack(pady=10)
    entry_su_user = tk.Entry(signup_window)
    entry_su_user.pack()
    tk.Label(signup_window, text="Password:").pack(pady=10)
    entry_su_pass = tk.Entry(signup_window, show="*")
    entry_su_pass.pack()
    tk.Button(signup_window, text="Signup", command=signup, bg="green", fg="white").pack(pady=20)

# ================== Login Window ==================
login_window = tk.Tk()
login_window.title("Library Login / Signup")
login_window.geometry("400x250")

tk.Label(login_window, text="Username:", font=("Arial", 12)).pack(pady=10)
entry_user = tk.Entry(login_window, font=("Arial", 12))
entry_user.pack()
tk.Label(login_window, text="Password:", font=("Arial", 12)).pack(pady=10)
entry_pass = tk.Entry(login_window, show="*", font=("Arial", 12))
entry_pass.pack()
tk.Button(login_window, text="Login", command=login, bg="green", fg="white").pack(pady=10)
tk.Button(login_window, text="Signup", command=open_signup, bg="blue", fg="white").pack()
login_window.mainloop()

# ================== Main GUI ==================
def main_gui(username):
    root = tk.Tk()
    root.title("Library Management System")
    root.state("zoomed")  # Fullscreen

    # Background Image
    bg_image = Image.open("Liberey_managment_system/ylswjsy7stw-scaled.jpg")  # Replace with your path
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
    root.bg_photo = ImageTk.PhotoImage(bg_image)  # Keep reference
    bg_label = tk.Label(root, image=root.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ================== Helper Functions ==================
    def fetch_books():
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()

    def show_book_details(book):
        msg = f"Title: {book[1]}\nAuthor: {book[2]}\nGenre: {book[4]}\nQuantity: {book[5]}"
        messagebox.showinfo("Book Details", msg)

    def display_books():
        for widget in frame_inner.winfo_children():
            widget.destroy()
        search_text = entry_search.get().lower()
        for book in fetch_books():
            if search_text in book[1].lower():
                btn = tk.Button(frame_inner, text=book[1], width=30, height=2, bg="lightblue",
                                command=lambda b=book: show_book_details(b))
                btn.pack(pady=5)
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="blue", fg="white"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="lightblue", fg="black"))

    # ================== Add Book Function ==================
    def add_book():
        def save_book():
            t = entry_title.get()
            a = entry_author.get()
            i = entry_isbn.get()
            g = entry_genre.get()
            q = entry_quantity.get()
            if t=="" or a=="" or q=="":
                messagebox.showerror("Error","Title, Author, Quantity required!")
                return
            cursor.execute("INSERT INTO books (title,author,isbn,genre,quantity) VALUES (?,?,?,?,?)",
                           (t,a,i,g,q))
            conn.commit()
            messagebox.showinfo("Success","Book added!")
            book_window.destroy()
            display_books()

        book_window = tk.Toplevel()
        book_window.title("Add Book")
        tk.Label(book_window,text="Title:").grid(row=0,column=0,pady=5)
        entry_title = tk.Entry(book_window)
        entry_title.grid(row=0,column=1,pady=5)
        tk.Label(book_window,text="Author:").grid(row=1,column=0,pady=5)
        entry_author = tk.Entry(book_window)
        entry_author.grid(row=1,column=1,pady=5)
        tk.Label(book_window,text="ISBN:").grid(row=2,column=0,pady=5)
        entry_isbn = tk.Entry(book_window)
        entry_isbn.grid(row=2,column=1,pady=5)
        tk.Label(book_window,text="Genre:").grid(row=3,column=0,pady=5)
        entry_genre = tk.Entry(book_window)
        entry_genre.grid(row=3,column=1,pady=5)
        tk.Label(book_window,text="Quantity:").grid(row=4,column=0,pady=5)
        entry_quantity = tk.Entry(book_window)
        entry_quantity.grid(row=4,column=1,pady=5)
        tk.Button(book_window,text="Save",command=save_book,bg="green",fg="white").grid(row=5,column=1,pady=10)

    # ================== GUI Elements ==================
    tk.Label(root, text=f"Welcome {username}!", font=("Arial", 20), bg="#ffffff").place(x=50, y=20)
    tk.Label(root, text="Search Book:", font=("Arial", 14), bg="#ffffff").place(x=50, y=70)
    entry_search = tk.Entry(root, font=("Arial", 14), width=30)
    entry_search.place(x=180, y=70)
    tk.Button(root, text="Search", font=("Arial", 12), command=display_books, bg="green", fg="white").place(x=500, y=68)
    tk.Button(root, text="Add Book", font=("Arial", 12), command=add_book, bg="blue", fg="white").place(x=600, y=68)

    # ================== Scrollable Frame ==================
    canvas = tk.Canvas(root, bg="#ffffff", width=600, height=600)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#ffffff")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.place(x=50, y=120)
    scrollbar.place(x=650, y=120, height=600)
    frame_inner = scrollable_frame

    display_books()
    root.mainloop()
main_gui()