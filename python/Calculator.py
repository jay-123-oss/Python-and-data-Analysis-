# this is normal used calculator by used python 





combo = ["adition","sub","multi","divi","agv"]

input1 = int(input("enter any no.: "))
input2 = int(input("enter second no.: "))

while True:
 another = str(input("another input(yes/no): " ))
 if another == "yes":
     input3 = int(input("enter any no.: "))
 elif another == "no":
    input3 = 0
    method = input("enter opretion: ")
    if method == "adition":
      print(input1+input2+input3)
         
    else:
      pass
    if method == "sub":
      print(input1-input2-input3)
    else:
      pass
    if method == "multi":
      print(input1*input2*input3)
    else:
      pass
    if method == "divi":
      print(input1/input2/input3)
    else:
      pass
    if method == "agv":
      print(input1+input2+input3)/2
    else:
     print("invailed opretion.")
    
 
    



    

 



