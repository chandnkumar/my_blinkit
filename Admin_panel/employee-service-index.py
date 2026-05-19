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

    # ================= INSERT =================
    if v == 'load':
        url="select user_id from tbl_employeedetail"
        x.execute(url)
        res=x.fetchall()
        # print(url)
        # print(res)
        if res==[]:
            print("No records found")
        else:
            s1=""
            for a in res:
                s1+="<option value='"+str(a[0])+"'>"+str(a[0])+"</option>"
                print(s1)
                
            

    # ================= SEARCH =================
    elif v == 'search':
        a = fs.getvalue('t1')  # user_id
        b = fs.getvalue('t2')  # full_name
        c = fs.getvalue('t3')  # contact_no
        d = fs.getvalue('t4')  # role
        e = fs.getvalue('t5')  # status

        url = "select * from tbl_employeedetail where "
        k = len(url)

        if a != None:
            url = url + "user_id=\'" + str(a) + "\'"

        if b != None:
            if k == len(url):
                url = url + "full_name=\'" + str(b) + "\'"
            else:
                url = url + " and full_name=\'" + str(b) + "\'"

        if c != None:
            if k == len(url):
                url = url + "contact_no=\'" + str(c) + "\'"
            else:
                url = url + " and contact_no=\'" + str(c) + "\'"

        if d != None:
            if k == len(url):
                url = url + "role=\'" + str(d) + "\'"
            else:
                url = url + " and role=\'" + str(d) + "\'"

        if e != None:
            if k == len(url):
                url = url + "status=\'" + str(e) + "\'"
            else:
                url = url + " and status=\'" + str(e) + "\'"

        x.execute(url)
        res = x.fetchall()

        if res == []:
            print("<div class='alert alert-warning'>No records found</div>")
        else:
            print("""<table class='table table-bordered'><tr style='background-color: gray; color:white;'><th>User ID</th><th>Full Name</th><th>Contact</th><th>Email</th><th>Role</th><th>Status</th><th>Address</th><th>id_proof</th><th>profile_image</th><th>Action</th></tr>""")

            for a in res:
                # pic=adh=""
                # if a[7] is not None:
                #     id_proof=base64.b64encode(a[7]).decode('utf-8')
                #     id_proof="<img src='data:image/jpeg;base64,"+id_proof+"' width='60' height='60'/>"
                # if a[8]:
                #     profile_img=base64.b64encode(a[8]).decode('utf-8')
                #     profile_img="<img src='data:image/jpeg;base64,"+profile_img+"' width='60' height='60'/>"
                # else:
                #     profile_img = "N/A"
                id_proof = "N/A"
                profile_img = "N/A"

                if a[7] is not None:
                    img1 = base64.b64encode(a[7]).decode('utf-8')
                    id_proof = "<img src='data:image/jpeg;base64," + img1 + "' width='60' height='60'/>"

                if a[8] is not None:
                     img2 = base64.b64encode(a[8]).decode('utf-8')
                     profile_img = "<img src='data:image/jpeg;base64," + img2 + "' width='60' height='60'/>"
                print(f"<tr><td>" + str(a[0]) + "</td><td>" + str(a[1]) + "</td><td>" + str(a[2]) + "</td><td>" + str(a[3]) + "</td><td>" + str(a[4]) + "</td><td>" + str(a[5]) + "</td><td>" + str(a[6]) + "</td><td>"+id_proof+"</td><td>"+profile_img+"</td><td><i class=' upd fa-solid fa-pen-to-square text-primary'> </i> <i class=' del fa-solid fa-trash text-danger ms-2'></i></td></tr>")

            print("</table>")
            
            
        
        # my new code
        
        # if res == []:
        #     print("""
        #         <div class="row">
        #         <div class="col-lg-12">
        #         <div class="card stretch stretch-full">
        #         <div class="card-body lead-status">
        #             <div class="alert alert-info fs-5 fw-bolder px-2 py-1">Employee Record :-</div>
        #             <div class="alert alert-warning color-red">No record</div>
        #             </div>
        #         </div>
        #         </div>
        #         </div>
        #         """)
    
        # else:
        #      print("""
        #         <div class="row">
        #         <div class="col-lg-12">
        #         <div class="card stretch stretch-full">
        #         <div class="card-body lead-status">
        #             <div class="alert alert-info fs-5 fw-bolder px-2 py-1">Employee Record :-</div>

        #             <table class="table table-bordered">
        #                 <thead>
        #                     <tr>
        #                         <th>User_Id</th>
        #                         <th>Full_Name</th>
        #                         <th>Contact No</th>
        #                         <th>Email</th>
        #                         <th>Role</th>
        #                         <th>Status</th>
        #                         <th>Address</th>
                                
        #                         <th>Action</th>
        #                     </tr>
        #                 </thead>
        #                 <tbody>
        #                      """)

        #      for a in res:
        #         print(f"""
        #             <tr>
        #             <td>{a[0]}</td>
        #             <td>{a[1]}</td>
        #             <td>{a[2]}</td>
        #             <td>{a[3]}</td>
        #             <td>{a[4]}</td>
        #             <td>{a[5]}</td>
        #             <td>{a[6]}</td>
                    
        #             <td>
        #                 <a href="#" class="text-primary">
        #                     <i class="fa-solid fa-pen-to-square"></i>
        #                 </a>
        #                 <a href="#" class="ms-3 text-danger">
        #                     <i class="fa-solid fa-trash"></i>
        #                 </a>
        #             </td>
        #             </tr>
        #             """)

        #         print("""
        #             </tbody>
        #             </table>

        #             </div>
        #             </div>
        #             </div>
        #             </div>
        #             """)


    # elif v=="update":
    #     # print("hi")
    #     url="update tbl_employeedetail set full_name=\'"+str(fs.getvalue('t2'))+"\',contact_no=\'"+str(fs.getvalue('t3'))+"\',email=\'"+str(fs.getvalue('t4'))+"\',role=\'"+str(fs.getvalue('t5'))+"\',status=\'"+str(fs.getvalue('t6'))+"\',address=\'"+str(fs.getvalue('t7'))+"\',id_proof=\'"+(fs['t8'].file.read())+"\',profile_image=\'"+fs['t9'].file.read()+"\' where user_id=\'"+str(fs.getvalue('t1'))+"\'"
    #     # print(url)
    #     x.execute(url)
    #     con.commit() 
    #     print(1)
    
    elif v == "update":

     sql = """UPDATE tbl_employeedetail 
              SET full_name=%s, contact_no=%s, email=%s, role=%s,
                  status=%s, address=%s"""
 
     val = [
         fs.getvalue('t2'),
         fs.getvalue('t3'),
         fs.getvalue('t4'),
         fs.getvalue('t5'),
         fs.getvalue('t6'),
         fs.getvalue('t7')
     ]
 
     # ✅ image 1
     if 't8' in fs and fs['t8'].filename:
         img1 = fs['t8'].file.read()   # bytes ✔
         sql += ", id_proof=%s"
         val.append(img1)
 
     # ✅ image 2
     if 't9' in fs and fs['t9'].filename:
         img2 = fs['t9'].file.read()   # bytes ✔
         sql += ", profile_image=%s"
         val.append(img2)
 
     sql += " WHERE user_id=%s"
     val.append(fs.getvalue('t1'))
 
     x.execute(sql, tuple(val))   # ✔ safe
     con.commit()
     print(1)
    
        
    # elif v=="delete": 
    else:
        url="delete from tbl_employeedetail where user_id='"+str(fs.getvalue('t1'))+"'"
        # print(url)
        x.execute(url)
        con.commit()
        print(1)
        
    
        
except Exception as error:
    print(error)
    print("Unsuccess")

con.close()