n=int(input())
num1,num2=0,1
i=0
print("FIBONACCI SERIES")
while(i<n):
    print(num1, end=" ")
    res=num1+num2
    num1=num2
    num2=res
    i+=1