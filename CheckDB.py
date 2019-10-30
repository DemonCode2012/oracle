import cx_Oracle as ora
import time
import Sys_login


def checkdb(ip, port, tnsnm):
    try:
        conn = Sys_login.syslogin(tnsnm)

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
