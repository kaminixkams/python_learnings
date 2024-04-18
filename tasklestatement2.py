word=input("Enter the sentence: ")
a=len(word)
b=a//2
l=0
if a%2==0:
    for i in range(1,b+1):
        l+=i
    print(l)
else:
    for i in range(1,a+1):
        l+=i
    print(l)
