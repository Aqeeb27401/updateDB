import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="",database="aqeeb")
Cursor=con.cursor()
Cursor.execute("UPDATE `emp` SET `salary` = '75' WHERE `emp`.`code` = 7");
con.commit()
print("Sucessfully updated")