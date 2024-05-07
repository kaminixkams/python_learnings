task 2
a=input().split()
if a[0].isalpha() and a[1].isnumeric and a[2].isalpha() and a[3].isnumeric:
    print("True")
else:
    print("False")



task1
a=int(input())
number=[]
for i in range(-a,a+1):
    number.append(i)
print(number)



task4
existing_states=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgrah","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal"]
state=input("Enter a letter: ")
l=[]
for i in existing_states:
                 if i[0]==state:
                     l.append(i)
existing_states.sort(key=len, reverse=True)
print(existing_states)

for i in existing_states:
    print(i,len(i))



task3
existing_states=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgrah","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal"]
state=input("Enter a letter: ")
for i in existing_states:
                 if i[0]==state:
                     print(i)

task5
a=input("Enter a number: ")
k=0
for i in a:
    k+=int(i)**3
if int(a)==k:
    print(k,"It is an armstrong number")
else:
    print(k,"It is not an armstrong number")






