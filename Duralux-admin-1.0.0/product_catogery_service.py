#!C:\Users\HP\AppData\Local\Programs\Python\Python39-32\python.exe
print("Content-Type: text/html\n")

import cgi
import mysql.connector
import base64 #for image display


# DB connection
con = mysql.connector.connect(
    host="localhost",
    user="blinkit",
    password="chandan@123",
    database="blinkit"
)

x = con.cursor()
fs = cgi.FieldStorage()
 
try:
    v = fs.getvalue('t')
    # print(v)
    if v == 'loade':
       pass
   
    elif v=='search':
        a=fs.getvalue('t1')
        b=fs.getvalue('t2')
        url="select * from tbl_product_catogery where "
        k=len(url)
        
        if a!=None:
            url=url+"catogery_id=\'" + str(a) + "\'"
            
        if b != None:
            if k == len(url):
                url = url + "catogery_name=\'" + str(b) + "\'"
            else:
                url = url + " and catogery_name=\'" + str(b) + "\'"
                
        # print(url)
        x.execute(url)
        res=x.fetchall()
        
        if res == []:
            print("<div class='alert alert-warning'>No records found</div>")
        else:
            print("""<table class='table table-bordered'><tr style='background-color: gray; color:white;'><th>Catogery ID</th><th>Catogery Name</th><th>Catogery image</th><th>Description</th><th>Action</th></tr>""")

            for a in res:
               
            #     if a[2] is not None:
            #         catogery_img="<img src='data:image/jpeg;base64,"+catogery_img+"' width='60' height='60'/>"
            #         catogery_img=base64.b64encode(a[2]).decode('utf-8')
            #     print(f"<tr><td>" + str(a[0]) + "</td><td>" + str(a[1]) + "</td><td>" + catogery_img + "</td><td>" + str(a[3]) + "</td><td><td><i class='fa-solid fa-pen-to-square text-primary'> </i> <i class='fa-solid fa-trash text-danger ms-2'></i></td></tr>")

            # print("</table>")
            
             # Default image value
                catogery_img = "No Image"

                if a[2] is not None:
                    img_data = base64.b64encode(a[2]).decode('utf-8')
                    catogery_img = f"<img src='data:image/jpeg;base64,{img_data}' width='60' height='60'/>"

                    print(f"""
                    <tr>
                        <td>{a[0]}</td>
                        <td>{a[1]}</td>
                        <td>{catogery_img}</td>
                        <td>{a[3]}</td>
                        <td>
                            <i class='fa-solid fa-pen-to-square text-primary'></i>
                            <i class='fa-solid fa-trash text-danger ms-2'></i>
                        </td>
                    </tr>
                    """)

            print("</table>")
       
       
except:
    print("unsuccess")