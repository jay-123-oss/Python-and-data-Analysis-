import random
while True:
    pass_len = int(input("Enter password len: "))
    char = "mnbvcxzlkjhgfdsaqwertyuiopQWERTYUIOPLKJHGFDSAZXCVBNM0123456789!@#$%&*./?"
    password = "".join(random.sample(char, pass_len))
    if pass_len <= 72:
        print(f"__________{password}_________")
    elif pass_len > 72:
        print("choose any no, 1 to 72")
        break