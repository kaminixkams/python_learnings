




word=len(input("Enter a word: "))
table=(word//2)

if word%2==0:
    for i in range(1,word+1):
        print(i*table)

else:
    for i in range(1,word+1):
        print(i*word)
    


