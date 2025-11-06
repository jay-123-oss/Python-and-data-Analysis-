print("_______________wellcome to quiz session_______________")
input_user = input("you are redy:(yes/no):  ")
main_list = [" James Gosling"," Guido van Rossum" ," Dennis Ritchie","Bjarne Stroustrup","[]","()","{}","<>","*","-","+","&"," Comment likhne ke liye"," Code ko fast karne ke liye"," Code blocks define karne ke liye "," Variable banane ke liye","6","8","9","error","Immutable","Mutable","Both","None","read()","scanf()","input()","get()","Python 3.8",
]

marksheet = 0
if input_user == "yes":
    # question no. 1
    print("Q1. Python ka creator kaun hai?")
    input_1 = input("enter ans: ")
    
    if input_1 in main_list:
        if input_1 == "Guido van Rossum":
            print("correct ans.")
            marksheet+=5
        else:
            print("wrong ans")
    # question no. 2
    print(" Q2. Python me list banane ke liye kaunsa symbol use hota hai?")
    input_2 = input("enter ans 2: ")
    if input_2 == "[]":
        print("correct ans.")
        marksheet+=5
    else:
       print("wrong ans")
    # question no. 3
    print("Python me string ko concatenate karne ke liye kaunsa operator use hota hai?")
    input_3 = input("enter ans: ")
    if input_3 == "+" :
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans")
    # question no. 4
    print("Q4. Python me indentation ka use kis liye hota hai?")
    input_4 = input("enter ans: ")
    if input_4 == "Code blocks define karne ke liye":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 5
    print("Q5. Python me “print(23)” ka output kya hoga?**")
    input_5 = input("enter ans: ")
    if input_5 == "8":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 6
    print("Q6. Python me tuple immutable hota hai ya mutable?")
    input_6 = input("enter ans: ")
    if input_6 == "Immutable":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 7
    print("Q7. Python me dictionary ko kaise represent karte hai?")
    input_7 = input("enter ans: ")
    if input_7 == "{}":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 8
    print("Q8. Python me input lene ke liye kaunsa function use hota hai?")
    input_8 = input("enter ans: ")
    if input_8 == "input()":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 9
    print("Q9. Python ka latest stable version 2025 me kaunsa hai?")
    input_9 = input("enter ans: ")
    if input_9 == "Python 3.13":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    # question no. 10
    print("Q10. Python me “len(‘Hello’)” ka output kya hoga?")
    input_10 = input("enter ans: ")
    if input_10 == "5":
        print("correct ans.")
        marksheet+=5
    else:
        print("wrong ans.")
    print(f" congeratulation your is score is {int(marksheet)}.")
   

else:
    print("okay")






