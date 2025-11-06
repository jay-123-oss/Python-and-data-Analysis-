# hotel_menu.py 
menu = {
    'coffee': 50,
    'tea': 20,
    'burger': 100,
    'pizza': 150,
    'water': 10,
    'samosa': 15,
}

print("Welcome to the Hotel Menu")
print("coffee: Rs50\ntea: Rs20\nburger: Rs100\npizza: Rs150\nwater: Rs10\nsamosa: Rs15")

order_total = 0

item1 = input("enter your first item: ")
if item1 in menu:
    order_total += menu[item1]
    print(f"your order {item1} has been added your olrder")
else:
    print("Sorry, we don't have that item.")  

while True:
    another_item = input("do you want to add another item? (yes/no): ")
    if another_item.lower() != 'yes':
        break
    item = input("enter your next item: ")
    if item in menu:
        order_total += menu[item]
        print(f"your order {item} has been added to your order")
    else:
        print("Sorry, we don't have that item.")

print(f"your total order amount is Rs{order_total}")
print("Thank you for your order!")
print("take care and have a nice day!")
   
   # close the program 