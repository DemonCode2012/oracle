import cx_Oracle as ora
username = 'test'
password = 'abcd1234'
ip = '192.168.194.103'
port = '1521'
srvnm = 'orcl'

tnsnm = ora.makedsn(ip, port, service_name=srvnm)
conn = ora.connect(username, password, dsn=tnsnm)
print('Connection Success!')

curs = conn.cursor()

# sqlid = input("请输入sqlid: ")
sqlid = 'b7ghr8z9mm79s'
sqlplan = "select * from table(dbms_xplan.display_cursor('{}'))".format(sqlid)
# print(df)
rr = curs.execute(sqlplan)
for result in rr:
    if ''.join(result) != ' ':
        print(''.join(result))
