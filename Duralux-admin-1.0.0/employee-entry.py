#!C:\Users\HP\AppData\Local\Programs\Python\Python39-32\python.exe
print("Content-Type: text/html\n")
import cgi
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="blinkit",
    password="chandan@123",
    database="blinkit"
)
x=conn.cursor()

t=cgi.FieldStorage()
try:
    v1=t.getvalue('t1')
    v2=t.getvalue('t2')
    v3=t.getvalue('t3')  
    v4=t.getvalue('t4')
    v5=t.getvalue('t5')
    v6=t.getvalue('t6')
    v7=t.getvalue('t7') 
    v8=t['t8'].file.read()
    v9=t['t9'].file.read()
    if(v9=='none'):
        url="insert into tbl_employeedetail(user_id,full_name,contact_no,email,role,status,address,id_proof) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        x.execute(url,(v1,v2,v3,v4,v5,v6,v7,v8))
        
    else:
        url="insert into tbl_employeedetail(user_id,full_name,contact_no,email,role,status,address,id_proof,profile_image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        x.execute(url,(v1,v2,v3,v4,v5,v6,v7,v8,v9))
    conn.commit()
    print(1)
except:
    print("unsucess")  
    
    
    
    