# Author Adarsh 
# import section
import mysql.connector
# connection to db
db= mysql.connector.connect(

	host = "172.16.11.46",
	user = "dbadmin",
	passwd = "VICI@eos",
    database="FileInput"
    )
mycursor = db.cursor()
# Query For fetching data
sql_select_Query = "select * from files"
# fetchall For fetching all the data present in table
mycursor.execute(sql_select_Query)
records = mycursor.fetchall()
# mycursor.rowcount will gives us total rows present in table 
print("Total number of rows in table: ", mycursor.rowcount)
# to get each data 
for row in records:
    print("[Id] = ", row[0], )
    print("FileName = ", row[1])
    print("FilePath  = ", row[2])
    print("ExecutionTime  = ", row[3])
    print("DateTime  = ", row[4])
    print("Exe_Status  = ", row[5], "\n")
    if  row[5] ==1:
        print("not executed")
#         os.rename("temp.txt","Astrix.txt")

# ccheck connection
if db.is_connected():
#     close db connection
    db.close()
    mycursor.close()
    print("connection is closed")
