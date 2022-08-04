'''
# Write a file in python 
with open('Astrix.txt', 'a') as f:
    f.write('1~')
    f.write('Name~')
    f.write('Emp_id~')
    f.write('Role~')
    f.write('contact')
f.close()

#find specific word in txt file 
file = open("WriteAstrix.txt")
print(file.read())
search_word = input("enter a word you want to search in file: ")
if(search_word in file.read()):
    print("word found")
else:
    print("word not found")
with open('example.txt') as f:
    if 'blabla' in f.read():
        print("true")
        
#find specific word in txt file 
with open('WriteAstrix.txt') as f:
    
    search_word = input("enter a word you want to search in file: ")
    if search_word in f.read():
        print("true")
        
    else:
        print("false")

f = open('WriteAstrix.txt')
content = f.readlines()
print(content[9])

'''
import os

fh_r = open("Astrix.txt", "r")
fh_w = open("temp.txt", "w")

index = input("Enter the index no to Search:")

s =' '
while(s):
    s=fh_r.readline()
    L=s.split("~")
    if len(s)>0:
        if L[0]==index:
            i_d = index
            Name=input("Enter a Name")
            Emp_id=input("Enter a Emp_id")
            Role=input("Enter a Role")
            contact=input("Enter a contact")
            fh_w.write(i_d+"~"+Name+"~"+Emp_id+"~"+Role+"~"+contact+"\n")
        else:
            print("we ARE IN ELSE")
            fh_w.write(s)

fh_w.close()
fh_r.close()
os.remove("Astrix.txt")
os.rename("temp.txt","Astrix.txt")
