with open('currency.txt') as f:
    lines = f.readlines()
currencydict = {}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]] = parsed[1]

amount = int(input("enter amount: \n"))  # <-- fixed input
print("enter name of currency: ")
[print(item) for item in currencydict.keys()]
currency = input("enter name of currency: ")
print(f"{amount} INR is equal to {amount * float(currencydict[currency])} {currency}")