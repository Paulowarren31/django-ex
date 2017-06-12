import cx_Oracle

connection_string = 'paulowar/Pw6517nP@pinntst.dsc.umich.edu:1521/pinndev.world'

conn = cx_Oracle.connect(connection_string)
cursor = conn.cursor()

query = "select * from um_ecomm_dept_units_rept where deptid between 0 and 99999"

cursor.execute(query)

for row in cursor:
  print row
