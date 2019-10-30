import cx_Oracle as ora
import time

username = 'test'
password = 'abcd1234'
ip = '192.168.194.103'
port = '1521'
srvnm = 'orcl'

tnsnm = ora.makedsn(ip, port, service_name=srvnm)

##########################################################################################
try:
    conn = ora.connect('sys', 'abcd1234', dsn=tnsnm, mode=ora.SYSDBA)

    # 输出客户端版本
    verc = list(ora.clientversion())
    verc = [str(x) for x in verc]
    print('Client Version is ', end='')
    print('.'.join(verc))

    # 输出服务端版本
    print('Server Version is {}'.format(conn.version))

    curs = conn.cursor()

    # 输出数据库状态和启动时间
    sql = 'select instance_name,instance_number,startup_time,status from gv$instance order by inst_id'
    rr = curs.execute(sql)
    for result in rr:
        instno = result[0]
        instnm = result[1]
        starttm = result[2]
        stat = result[3]
        print('实例{}:{}在{}启动，状态是{}'.format(instnm, instno, starttm, stat))

except ora.DatabaseError as exc:
    # 给变量名为error的赋值异常码
    error, = exc.args
    time_now = (time.strftime("%Y%m%d %H:%M:%S", time.localtime()))
    print("数据库错误代码: {}\n发生错误时间为: {}\n发生错误的数据库IP为: {}:{}".format(error.message, time_now, ip, port))
    print("无法确定数据库状态!")

##########################################################################################
try:
    conn = ora.connect(username, password, dsn=tnsnm)
    print('Connection Success!')

    curs = conn.cursor()

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

##########################################################################################
