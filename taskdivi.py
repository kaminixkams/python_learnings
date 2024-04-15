num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
print("1")
for i in range (1,num3+1):
    if (i%num1==0 and i%num2==0):
        print(i)
