#taking an integer input  from user
num=int(input("ENTER A NUMBER: "))
i=1 #looping variable
j=1 #looping variable
product=1 #variable to calculate the products
title="MULTIPLICATION TABLE" #title of the output
print()
print(title)
print("______________")
print()
while j<=num:
    for i in range(1,11):
        product=j*i #calculating the products
        print("{} x {} = {}".format(j,i,product)) #printing the multiplication table
    print("______________")
    print()
    j=j+1