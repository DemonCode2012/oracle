import cx_Oracle as ora
import time
# import getpass

import CheckDB
import Choice
# import window_login

username = 'c##ly'
password = 'abcd1234'
ip = '192.168.194.105'
port = '1521'
srvnm = 'pdb'
print("Logging on database ...")

# username = input("username:")
# password = getpass.getpass("password:")
# ip = input("ip:")
# port = input("port:")
# srvnm = input("service_name:")

tnsnm = ora.makedsn(ip, port, service_name=srvnm)
# print(tnsnm)

CheckDB.checkdb(ip, port, tnsnm)

try:
    conn = ora.connect(username, password, dsn=tnsnm)
    print('Connection Success!')

    curs = conn.cursor()

    if Choice.choice(curs, conn):
        curs.close()
        conn.close()
        print('Bye !')
        exit()

except ora.DatabaseError as exc:
    # 给变量名为error的赋值异常码
    print('***** 连接/查询 失败！ *****')
    error, = exc.args
    time_now = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
    print("数据库错误代码: {}\n发生错误时间为: {}\n发生错误的数据库IP为: {}:{}".format(error.message, time_now, ip, port))
    if error.code == 1017:
        print('请检查用户密码！')
    elif error.code == 942:
        print('请检查用户权限！')
    # ORA-12899: value too large for column
