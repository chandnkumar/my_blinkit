#!C:\Users\HP\AppData\Local\Programs\Python\Python39-32\python.exe
print("Content-Type: text/html\n")

# print("hi hello")
import cgi
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="blinkit",
    password="chandan@123",
    database="blinkit"
)
x=conn.cursor()

f=cgi.FieldStorage()
try:
    v=f.getvalue('t')
    if v=="signup":
        a=f.getvalue('t1')
        b=f.getvalue('t2')
        c=f.getvalue('t3')
        d=f.getvalue('t4')
        e=f.getvalue('t5')
        # print(a,b,c,d,e)
        url="insert into signup_tbl (name,phone_no,email,pass,address) value (%s,%s,%s,%s,%s)"
        x.execute(url,(a,b,c,d,e))
        conn.commit()
        print(1)
        
    else:
        ab=f.getvalue('ta')
        bc=f.getvalue('tb')
        # print(ab,bc)
        url="select * from signup_tbl where email='"+str(ab)+"' and pass='"+str(bc)+"'"
        # print(url)
        x.execute(url)
        res=x.fetchall()
        # print(res)
        if res==[]:
            print(0)
        else:
            print(1)
        
except:
    print("unsucess")