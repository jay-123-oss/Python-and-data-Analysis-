    
while True:
    age=int(input("enter your age"))
    if age>100:
        print("pleas enter valied age")
    elif age>=18:
        print("your can vote")
    elif age<18 or age>3:
        print("you are schooling")
    else:
        pass