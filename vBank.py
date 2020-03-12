# try except 完善
# 账户不能为负数
# 注册功能未完成

import Choice
import datetime
import cx_Oracle as ora
import time


# 注册账号
def register(curs, conn):
    conn.commit()


# 登陆系统
def logon(curs, conn, account_id, passwd):
    global db_passwd
    logon_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(logon_date)
    check_pass = "select passwd from account where id = {}".format(account_id)
    for item in curs.execute(check_pass):
        db_passwd = item[0]
    if passwd == db_passwd:
        logon_status = 'Y'
        print("Logon Successfully!")
        choice(curs, conn, account_id, passwd)
    else:
        logon_status = 'N'
        print("Logon Failed!")
    logon_hist_insert = "insert into logon_hist values({},to_date('{}','yyyy-mm-dd hh24:mi:ss')," \
                        "'{}')".format(account_id, logon_date, logon_status)
    curs.execute(logon_hist_insert)
    conn.commit()


# 选择功能
def choice(curs, conn, account_id, passwd):
    cho = input("""请输入你要干啥：
    1.  存款
    2.  取款
    3.  转账
    4.  查询""")
    if cho == '1':
        deposit(curs, account_id)
    elif cho == '2':
        withdraw(curs, account_id)
    elif cho == '3':
        transfer(curs, account_id)
    elif cho == '4':
        sql_money = "select money from account where id={}".format(account_id)
        curs.execute(sql_money)
        money = curs.fetchone()[0]
        print("您账户的余额为 {} RMB".format(money))
    elif cho == '0':
        return True
    else:
        print("请重新登陆：")
        logon(curs, conn, account_id, passwd)


# 存款系统
def deposit(curs, account_id):
    amount = input("请输入存入的数额:")
    try:
        upd_money = "update account set money = money + {} where id={}".format(amount, account_id)
        curs.execute(upd_money)
    except:
        print('***** 连接/查询 失败！ *****')


# 取款系统
def withdraw(curs, account_id):
    amount = input("请输入取出的数额:")
    upd_money = "update account set money = money - {} where id={}".format(amount, account_id)
    curs.execute(upd_money)


# 转账系统
def transfer(curs, account_id):
    to_id = input("请输入您要转向的账户ID:")
    amount = input("请输入转账的数额:")
    from_money = "update account set money = money - {} where id={}".format(amount, account_id)
    to_money = "update account set money = money + {} where id={}".format(amount, to_id)
    try:
        curs.execute(from_money)
        curs.execute(to_money)
    except ora.DatabaseError as exc:
        # 给变量名为error的赋值异常码
        print('***** 连接/查询 失败！ *****')
        error, = exc.args
        time_now = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        print("数据库错误代码: {}\n发生错误时间为: {}\n".format(error.message, time_now))
        if error.code == 936:
            print('请重新输入！')
            transfer(curs, account_id)
        # ORA-12899: value too large for column


def vbank(curs, conn):
    reg = input("您是否已有账户：1.有 2.没有")
    if reg == '2':
        # 注册银行系统
        register(curs, conn)
    elif reg == '1':
        # 登陆银行系统
        id = input("请输入账号ID:")
        passwd = input("请输入账号密码:")
        logon(curs, conn, id, passwd)
        incont = input("是否继续:（输入1继续,输入0返回上一菜单,其他输入退出）")
        if incont == '1':
            choice(curs, conn, id, passwd)
        elif incont == '0':
            Choice.choice(curs, conn)
        else:
            return True



