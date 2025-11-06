booklist = {
    'Don Quixote': 'Miguel de Cervantes',
    "Alice's Adventures in Wonderland": 'Lewis Carroll',
    'The Adventures of Huckleberry Finn': 'Mark Twain',
    'The Adventures of Tom Sawyer': 'Mark Twain',
    'Treasure Island': 'Robert Louis Stevenson',
    'Pride and Prejudice': 'Jane Austen',
    'Wuthering Heights': 'Emily Brontë',
    'Jane Eyre': 'Charlotte Brontë',
    'Moby Dick': 'Herman Melville',
    'The Scarlet Letter': 'Nathaniel Hawthorne',
    "Gulliver's Travels": 'Jonathan Swift',
    "The Pilgrim's Progress": 'John Bunyan',
    'A Christmas Carol': 'Charles Dickens',
    'David Copperfield': 'Charles Dickens',
    'A Tale of Two Cities': 'Charles Dickens',
    'Little Women': 'Louisa May Alcott',
    'Great Expectations': 'Charles Dickens',
    'The Hobbit, or, There and Back Again': 'J.R.R. Tolkien',
    'Frankenstein, or, the Modern Prometheus': 'Mary Shelley',
    'Oliver Twist': 'Charles Dickens',
    "Uncle Tom's Cabin": 'Harriet Beecher Stowe',
    'Crime and Punishment': 'Fyodor Dostoyevsky',
    'Madame Bovary: Patterns of Provincial life': 'Gustave Flaubert',
    'The Return of the King': 'J.R.R. Tolkien',
    'Dracula': 'Bram Stoker',
    'The Three Musketeers': 'Alexandre Dumas',
    'Brave New World': 'Aldous Huxley',
    'War and Peace': 'Leo Tolstoy',
    'To Kill a Mockingbird': 'Harper Lee',
    'The Wizard of Oz': 'L. Frank Baum',
    'Les Misérables': 'Victor Hugo',
    'The Secret Garden': 'Frances Hodgson Burnett',
    'Animal Farm': 'George Orwell',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'The Little Prince': 'Antoine de Saint-Exupéry',
    'The Call of the Wild': 'Jack London',
    '20,000 Leagues Under the Sea': 'Jules Verne',
    'Anna Karenina': 'Leo Tolstoy',
    'The Wind in the Willows': 'Kenneth Grahame',
    'The Picture of Dorian Gray': 'Oscar Wilde',
    'The Grapes of Wrath': 'John Steinbeck',
    'Sense and Sensibility': 'Jane Austen',
    'The Last of the Mohicans': 'James Fenimore Cooper',
    "Tess of the d'Urbervilles": 'Thomas Hardy',
    "Harry Potter and the Sorcerer's Stone": 'J.K. Rowling',
    'Heidi': 'Johanna Spyri',
    'Ulysses': 'James Joyce',
    'The Complete Sherlock Holmes': 'Arthur Conan Doyle',
    'The Count of Monte Cristo': 'Alexandre Dumas',
    'The Old Man and the Sea': 'Ernest Hemingway',
    'Room': 'Emma Donoghue',
    'Deception Point': 'Dan Brown'
}

# -------------------- USER CLASS --------------------
class User:
    libname = "Jay Library"
    lib_addr = "ABD23, Bhopal"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def userinfo(self):
        if self.name.isalpha():
            print(f"\nHello {self.name}!")
            print(f"Name: {self.name}, Address: {self.address}")
        else:
            print("Please enter a valid name!")

# -------------------- BOOK CLASS --------------------
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def bookinfo(self):
        if self.name in booklist:
            print(f"\n'{self.name}' by {booklist[self.name]} is available.")
        else:
            print(f"'{self.name}' not found in library!")

# -------------------- MAIN PROGRAM --------------------
print(f"\nWelcome to {User.libname} - {User.lib_addr}")

u_name = input("Enter your name: ").strip()
u_addr = input("Enter your address: ").strip()

u = User(u_name, u_addr)
u.userinfo()

user_books = []

while True:
    print("\n------ Library Menu ------")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. View Your Account")
    print("4. Exit")

    try:
        ops = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if ops == 1:
        bookname = input("Enter book name: ").strip()
        authorname = input("Enter author name: ").strip()
        b = Book(bookname, authorname)
        b.bookinfo()

        if bookname in booklist:
            user_books.append(bookname)
            del booklist[bookname]
            print(f"'{bookname}' issued successfully!")

    elif ops == 2:
        bookname = input("Enter book name to return: ").strip()
        authorname = input("Enter author name: ").strip()
        if bookname in user_books:
            user_books.remove(bookname)
            booklist[bookname] = authorname
            print(f"'{bookname}' returned successfully!")
        else:
            print("You did not issue this book.")

    elif ops == 3:
        print("\n----- Your Account -----")
        print(f"Name: {u_name}")
        print(f"Address: {u_addr}")
        print(f"No. of Books Issued: {len(user_books)}")
        print(f"Books: {user_books if user_books else 'None'}")

    elif ops == 4:
        print("\nThank you for visiting Jay Library!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
