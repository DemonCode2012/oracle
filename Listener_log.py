import Choice
import time as tm


def listener_log(curs, conn):
    try:
        curs.execute("drop table lsnr_log purge")
        print("Drop Table Successfully!")
    except:
        pass
    curs.execute("create table lsnr_log (dttm date,ip varchar2(20),dbname varchar2(10),program varchar2(200),"
                 "hostname varchar2(100),username varchar2(50))")
    print("Create Table Successfully!")
    curs.execute("create index i_lsnr_log on lsnr_log(dttm)")
    print("Create Index Successfully!")

    # f_path = input("Path and name of log file :")
    f_path = r'D:\1.Project\python\oracle\listener.log'
    f = open(f_path, 'r')
    count = len(f.readlines())
    f.close()
    print("所选日志一共" + str(count) + "行.")

    time_start_tm = tm.localtime()
    time_start = tm.strftime("%Y%m%d %H:%M:%S", time_start_tm)
    print("Start inserting ... 开始时间为 {}".format(time_start))

    f = open(f_path, 'r')
    while 1:
        lines = f.readlines(10000)
        if not lines:
            break
        for line in lines:
            if ('establish' in line) and ('12502' not in line):
                # ##### time ##### #
                time = line[0:20]
                # print(time)

                # ##### ip ##### #
                start_pos_ip = line.rfind('HOST') + 5
                start_ip = line[start_pos_ip:]
                end_pos_ip = start_ip.find(')')
                ip = start_ip[:end_pos_ip]
                # print(ip)

                # ##### dbname ##### #
                end_pos_dbname = line.rfind('*') - 1
                start_pos_dbname = line.rfind('*', 0, end_pos_dbname)
                dbname = line[start_pos_dbname + 2:end_pos_dbname - 1]
                # print(dbname)

                # ##### program ##### #
                start_pos_program = line.find('PROGRAM') + 8
                start_program = line[start_pos_program:]
                end_pos_program = start_program.find(')')
                program = start_program[:end_pos_program]
                # print(program)

                # ##### hostname ##### #
                start_pos_hostname = line.find('HOST') + 5
                start_hostname = line[start_pos_hostname:]
                end_pos_hostname = start_hostname.find(')')
                hostname = start_hostname[:end_pos_hostname]
                # print(hostname)

                # ##### username ##### #
                start_pos_username = line.find('USER') + 5
                start_username = line[start_pos_username:]
                end_pos_username = start_username.find(')')
                username = start_username[:end_pos_username]
                # print(username)

                # ##### insert ##### #
                # print(line)
                curs.execute("insert into lsnr_log values"
                             "(to_date('{}','dd-MON-yyyy hh24:mi:ss'),"
                             "'{}','{}','{}','{}','{}')".format(time, ip, dbname, program, hostname, username))
                # print("insert into lsnr_log values"
                #       "(to_date('{}','dd-MON-yyyy hh24:mi:ss'),"
                #       "'{}','{}','{}','{}','{}')".format(time, ip, dbname, program, hostname, username))
        conn.commit()

    time_end_tm = tm.localtime()
    # print(type(time_end_tm))
    time_end = tm.strftime("%Y%m%d %H:%M:%S", time_end_tm)
    print("处理完成，请在数据库中查询 lsnr_log 表获得监听链接信息,结束时间为 {}".format(time_end))
    print("处理时间:{}秒".format(tm.mktime(time_end_tm)-tm.mktime(time_start_tm)))
    f.close()

    incont = input("是否继续处理日志文件：（输入1继续,输入0返回上一菜单,其他输入退出）")
    if incont == '1':
        listener_log(curs, conn)
    elif incont == '0':
        Choice.choice(curs, conn)
    else:
        return True
