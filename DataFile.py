import Choice


def ora_datafile(curs, conn):
    tbsnm = input("请输入表空间名：")
    df = "select rownum,file_name,bytes/1024/1024,AUTOEXTENSIBLE,maxbytes/1024/1024 from dba_data_files \
    where tablespace_name='{}' order by 1".format(tbsnm.upper())
    # print(df)
    rr = curs.execute(df)
    for result in rr:
        rowno = result[0]
        dfnm = result[1]
        dfsz = result[2]
        autoextensible = result[3]
        maxsz = result[4]
        if autoextensible == 'YES':
            print('表空间{}的第{}个数据文件路径是{},当前大小为{}MB,数据文件可扩展到{}MB。'.format(tbsnm, rowno, dfnm, dfsz, maxsz))
        else:
            print('表空间{}的第{}个数据文件路径是{},当前大小为{}MB,数据文件不可扩展。'.format(tbsnm, rowno, dfnm, dfsz))
    incont = input("是否继续查询数据文件：（输入1继续,输入0返回上一菜单,其他输入退出）")
    if incont == '1':
        ora_datafile(curs, conn)
    elif incont == '0':
        Choice.choice(curs, conn)
    else:
        return True
