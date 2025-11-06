# this is a rent claculator per person.
rent = int(input("enter rent : "))
food = int(input("enter food amount: "))
electricity = int(input("enter your ele. bill: "))
water = int(input('enter your water bill: '))
person = int(input("enter no. of person : "))

output = (rent+food+electricity+water)/person

print("per person bill is ",output)

