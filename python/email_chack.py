# Email chack....(wrong?/wright?)

email = input("enter your email: ")
k,j,d =0,0,0
if len(email) >=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):# j@j.in j@j.com
            if ("."in email) and ((email[-3]==".")^(email[-4]==".")):
                for i in email:
                    if i ==i.isspace:
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1:
                    print("wrong email !")
                
                      
            else:
                print("wrong email !")
            
        else:
            print("wrong email 1")
    else:
        print("wrong email !")
else:
    print("wrong email !")

