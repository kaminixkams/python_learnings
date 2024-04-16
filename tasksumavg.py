num1=int(input("Enter a num1: "))
value=0

for i in range(1,num1+1):
    a=int(input())
    value+=a 
if input("Enter sum or avg: ")=="sum":
    print(value)
else:
    print((value)/num1)
