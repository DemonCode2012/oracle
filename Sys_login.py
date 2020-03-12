import cx_Oracle as ora
# import getpass


def syslogin(tnsnm):
    # password = getpass.getpass("请输入sys密码，用于确认数据库状态：")
    password = input("请输入sys密码，用于确认数据库状态：")
    conn = ora.connect('sys', password, dsn=tnsnm, mode=ora.SYSDBA)
    return conn
