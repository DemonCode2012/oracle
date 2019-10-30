# ----- select ----- #
# sql = "SELECT * FROM tdata where rownum<100 order by id"  # sql语句
# rr = curs.execute(sql)
#
# rowall = rr
# for result in rowall:
#     print(result)
#
# # rowone = rr.fetchone()
# # print(rowone)
# rr.seek(0)
# rowmany = rr.fetchmany(numRows=3)
# print(rowmany)
#
# # print(row)
# curs.close()

# ----- insert select  ----- #
# truncate_t = "truncate table tdata"  # sql语句
# curs.execute(truncate_t)
# print('Truncate complete')
# insert_t = "insert into tdata select * from tpart"
# curs.execute(insert_t)
# print('Insert complete')
# conn.commit()
# print('Commit complete')
# curs.execute("""begin
# dbms_stats.gather_table_stats('TEST','TDATA',cascade=>true);
# end;""")
# print('Collect complete')

# ----- bind values ----- #
# named_params = {'dept_id': 50, 'sal': 1000}
# query1 = curs.execute('SELECT * FROM employees WHERE department_id=:dept_id AND salary>:sal', named_params)
# for i in query1:
#   print(i)

# query2 = curs.execute('SELECT * FROM employees WHERE department_id=:dept_id AND salary>:sal', dept_id=50, sal=1000)
# for i in query2:
#   print(i)
#
# print(curs.bindnames())

# curs.prepare('SELECT * FROM jobs WHERE min_salary>:min')
# r = curs.execute(None, {'min':1000})
# print(len(curs.fetchall()))

# create_table = """
# CREATE TABLE python_modules (
# module_name VARCHAR2(50) NOT NULL,
# file_path VARCHAR2(300) NOT NULL
# )
# """
# from sys import modules
# curs.execute(create_table)
# M = []
# for m_name, m_info in modules.items():
# 	try:
# 		M.append((m_name, m_info.__file__))
# 	except AttributeError:
# 		pass
# print(len(M))
#
# curs.prepare("INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)")
# curs.executemany(None, M)
# db.commit()
# r = curs.execute("SELECT COUNT(*) FROM python_modules")
# print(curs.fetchone())
# curs.execute("DROP TABLE python_modules PURGE")
