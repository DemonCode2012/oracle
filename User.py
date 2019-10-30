import Choice


def ora_user(curs):
    usr = "select username,default_tablespace,temporary_tablespace,account_status, \
    to_char(created, 'yyyymmdd hh24:mi:ss'), \
    to_char(LOCK_DATE, 'yyyymmdd hh24:mi:ss'), \
    to_char(EXPIRY_DATE, 'yyyymmdd hh24:mi:ss')  \
    from dba_users order by account_status,created"
    # print(df)
    rr = curs.execute(usr)
    for result in rr:
        username = result[0]
        deftbs = result[1]
        tmptbs = result[2]
        stat = result[3]
        created = result[4]
        lcdate = result[5]
        exdate = result[6]
        if stat[0:4] == 'OPEN':
            print('在{3}建立的用户{0}的默认表空间是{1},临时表空间是{2},当前状态为OPEN.'.format(username,deftbs, tmptbs, created))
        elif stat[0:6] == 'LOCKED':
            print('在{3}建立的用户{0}的默认表空间是{1},临时表空间是{2},当前状态为LOCKED,上锁时间为{4}.'.format(username, deftbs, tmptbs, created, lcdate))
        else:
            print('在{3}建立的用户{0}的默认表空间是{1},临时表空间是{2},当前状态为EXPIRED,过期时间为{4}.'.format(username, deftbs, tmptbs, created, exdate))
    incont = input("是否继续查询数据文件：（输入0返回上一菜单,其他输入退出）")
    if incont == '0':
        Choice.choice(curs)
    else:
        return True
