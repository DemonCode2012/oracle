import tkinter as tk
import tkinter.messagebox
import cx_Oracle as ora
import time

# import Main
import Choice

mainwin = tk.Tk()

# 主窗口
mainwin.title('OracleInfo')
mainwin.geometry('500x300')
maintext = tk.Label(mainwin, text='Oracle Information Collection', font=('黑体', 20))
maintext.pack()

# 输入信息标题
tk.Label(mainwin, text='IP ADDR', font=('黑体', 12)).place(x=50, y=60)
tk.Label(mainwin, text='IP PORT', font=('黑体', 12)).place(x=50, y=90)
tk.Label(mainwin, text='DB NAME', font=('黑体', 12)).place(x=50, y=120)
tk.Label(mainwin, text='USRNAME', font=('黑体', 12)).place(x=50, y=150)
tk.Label(mainwin, text='USRPASS', font=('黑体', 12)).place(x=50, y=180)

# 输入信息框
# IP地址
var_ip_addr = tk.StringVar()
entry_ip_addr = tk.Entry(mainwin, textvariable=var_ip_addr, font=('Arial', 14))
entry_ip_addr.place(x=150, y=60)
# 端口
var_ip_port = tk.StringVar()
entry_ip_port = tk.Entry(mainwin, textvariable=var_ip_port, font=('Arial', 14))
entry_ip_port.place(x=150, y=90)
# 实例名
var_db_name = tk.StringVar()
entry_db_name = tk.Entry(mainwin, textvariable=var_db_name, font=('Arial', 14))
entry_db_name.place(x=150, y=120)

ip = '192.168.194.1'
# port = 1521
srvnm = 'pdborcl'

# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(mainwin, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=150, y=150)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(mainwin, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=150, y=180)


def usr_login():
    ip = var_ip_addr.get()
    port = var_ip_port.get()
    srvnm = var_db_name.get()
    username = var_usr_name.get()
    password = var_usr_pwd.get()
    tnsnm = ora.makedsn(ip, port, service_name=srvnm)
    try:
        conn = ora.connect(username, password, dsn=tnsnm)
        # print('Connection Success!')

        curs = conn.cursor()

        if Choice.choice(curs):
            curs.close()
            conn.close()
            print('Bye !')
            exit()

    except ora.DatabaseError as exc:
        error, = exc.args
        time_now = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        # 给变量名为error的赋值异常码
        tk.messagebox.showerror(title='***** 连接/查询 失败！ *****', message="数据库错误代码: {}\n发生错误时间为: {}\n发生错误的数据库IP为: {}:{}".format(error.message, time_now, ip, port))
        # print('***** 连接/查询 失败！ *****')
        # print()
        # if error.code == 1017:
        #     print('请检查用户密码！')
        # elif error.code == 942:
        #     print('请检查用户权限！')


btn_login = tk.Button(mainwin, text='Login', command=usr_login).place(x=100, y=250)


mainwin.mainloop()
