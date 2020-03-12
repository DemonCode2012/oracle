import DataFile
import User
import Object
import Exp
import ExplainPlan
import Listener_log
import vBank


def choice(curs, conn):
    cho = input("""请选择你要查询你的信息：(输入序号即可,输入非序号输出)
    1.  表空间数据文件
    2.  用户
    3.  用户对象
    8.  查看执行计划
    10. 导出表数据为csv
    11. 处理监听日志
    21. 进入虚拟银行系统
    """)
    if cho == '1':
        DataFile.ora_datafile(curs, conn)
    elif cho == '2':
        User.ora_user(curs, conn)
    elif cho == '3':
        Object.ora_object(curs, conn)
    elif cho == '8':
        ExplainPlan.getplan(curs, conn)
    elif cho == '10':
        Exp.ora_exp(curs, conn)
    elif cho == '11':
        Listener_log.listener_log(curs, conn)
    elif cho == '21':
        vBank.vbank(curs, conn)
    else:
        return True
