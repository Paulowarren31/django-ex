import cx_Oracle

connection_string = 'paulowar/Pw6517nP@pinntst.dsc.umich.edu:1521/pinndev.world'

conn = cx_Oracle.connect(connection_string)
cursor = conn.cursor()

query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_grp_vp_area)"

vp_area = cursor.execute(query)

for row in  vp_area:
  print row

print 'ASDASDASDJJ'

query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_bud_seq)"

budget_seq = cursor.execute(query)

for row in  budget_seq:
  print row



