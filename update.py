import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="",database="aqeeb")
Cursor=con.cursor()
code=int(input("Enter code:"))
salary=int(input("Enter salary:"))
Cursor.execute("UPDATE `emp` SET `salary` = {} WHERE `emp`.`code` = {};".format(salary,code))
con.commit()
if Cursor.rowcount>0:
      print("Sucessfully updated")
else:
  print("No Data Found")
