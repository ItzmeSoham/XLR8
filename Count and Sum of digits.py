n=int(input("ENTER A NUMBER: "))
count=0
digit=1
Sum=0
while(n>0):
    digit=n%10
    count=count+1
    Sum=Sum+digit
    n=n//10
print("NO. OF DIGITS= ",count)
print("SUM OF DIGITS= ",Sum)