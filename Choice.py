import DataFile
import User
import Object
import Exp
import ExplainPlan


def choice(curs):
    cho = input("""请选择你要查询你的信息：(输入序号即可,输入非序号输出)
    1.  表空间数据文件
    2.  用户
    3.  用户对象
    8.  查看执行计划
    10. 导出表数据为csv
    """)
    if cho == '1':
        DataFile.ora_datafile(curs)
    elif cho == '2':
        User.ora_user(curs)
    elif cho == '3':
        Object.ora_object(curs)
    elif cho == '8':
        ExplainPlan.getplan(curs)
    elif cho == '10':
        Exp.ora_exp(curs)
    else:
        return True
