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
    v3=t['t3'].file.read()
    v4=t.getvalue('t4')
    
    # print(v1,v2,v3,v4)
    url=" insert into tbl_product_catogery(catogery_id,catogery_name,catogery_image,catogery_description) values (%s,%s,%s,%s) "
    x.execute(url,(v1,v2,v3,v4))
    conn.commit()
    print(1)
    

except:
    print("unsucess")