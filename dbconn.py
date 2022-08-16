# Author Adarsh 
# code for Update a .txt File Usimg Python 
# And Store its record to database 

import mysql.connector
import os
import time
import sys
from datetime import datetime

status = 0 

db= mysql.connector.connect(

	host = "172.16.11.46",
	user = "dbadmin",
	passwd = "VICI@eos",
    database="FileInput"
    )
mycursor = db.cursor()

# FileName = 'text2.text'
# FilePath = 'var/html/www/text2.text'
# ExecutionTime = 1660629063.1407458


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
#             print("we ARE IN ELSE")
            fh_w.write(s)

fh_w.close()
fh_r.close()
os.remove("Astrix.txt")
# get exact execution time
et = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
# print(et)
# exit()
# FileName = str(et)+"_"+".txt"
FileName = "temp.txt" 
# rename temp file to new name 
# os.rename("temp.txt",FileName)
# os.remove("temp.txt")
# get absolute path of file saving
FilePath = os.path.abspath(FileName)
print(FilePath)
# sys.exit()
# change File Name
os.rename("temp.txt","Astrix.txt")
# print(et)

if status != 0:
    print('There Must Be Some Issue!')
else:
    status = 1
    mycursor.execute('INSERT INTO files (FileName,FilePath,ExecutionTime,Exe_Status) VALUES (%s, %s, %s, %s)',(FileName,FilePath,et,status))
    db.commit()
    db.close()
    print(et)
    print("file updated sucessfully")
#     print(status)
