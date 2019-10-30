
import Choice
import Print_csv


def ora_exp(curs):
    tbnm = input("请输入表名：").upper()
    if tbnm == '':
        ora_exp(curs)

    # 格式化时间
    nls_format = "alter session set nls_date_format='yyyymmdd hh24:mi:ss' "
    curs.execute(nls_format)

    # 获得列名称
    usr_tb_col = """select column_id,column_name
    from user_tab_columns
    where table_name='{0}'
    order by 1""".format(tbnm.upper())
    rr = curs.execute(usr_tb_col)
    dictcol = {}
    for result in rr:
        dictcol[result[0]] = result[1]
    try:
        for i in range(1, len(dictcol)+1):
            print('{}.{}'.format(i, dictcol[i]))
    except KeyError:
        print('\n')
    listdict = list(dictcol.values())

    # 获得打印列名
    # printsql = ''
    # SelectCol.selectcol(curs, printsql, tbnm)
    global printsql
    colid = input("输入列编号，用逗号分割，*代表所有列,空值则返回上一菜单")
    cond = input("输入条件：（需要where关键字,不带分号）")

    sqlcount = """select count(*) from {} {}""".format(tbnm, cond)
    rr = curs.execute(sqlcount)
    count = rr.fetchone()
    print(count[0])

    # 生成具体sql
    if colid == '*':
    #     colsql = """select 'select '||col||' from '||table_name from (
    # SELECT table_name, LISTAGG(column_name, '||'',''||') WITHIN GROUP (ORDER BY column_id) AS col
    # FROM   user_tab_columns where table_name='{0}'
    # GROUP BY table_name)""".format(tbnm)
        printsql = """select * from {} {}""".format(tbnm, cond)
        # rr = curs.execute(colsql)
        # for r in rr:
        #     printsql = r[0] + ' ' + cond
    elif colid == '':
        ora_exp(curs)
    else:
        colid = colid.split(',')
        listcol = ''
        for i in range(len(colid)):
            if not colid[i].isdigit():
                printsql = ''
                break
            else:
                if eval(colid[i]) > max(dictcol.keys()):
                    break
                else:
                    listcol = listcol + "," + listdict[eval(colid[i])-1]
        if listcol == '':
            printsql = ''
        else:
            printsql = "select {0} from {1} {2}".format(listcol[1:], tbnm, cond)

    # for i, chunk in enumerate(chunks(cur)):
    #     f_out.write('\n'.join([column_delimiter.join(row[0]) for row in chunk]))
    #     f_out.write('\n')

    # dictcol.values()
    if printsql == '':
        print("Error!")
    else:
        print(printsql)
    # rr = curs.execute(printsql)
    # for i in range(1):
    #     print(rr)

    # for row_data in curs:
    #     if not row_data[0].startswith('BIN$'):  # skip recycle bin tables
    #         tableName = row_data[0]
    #

    Print_csv.print_csv(curs, tbnm, printsql, count)

    incont = input("是否继续导出表：（输入1继续,输入0返回上一菜单,其他输入退出）")
    if incont == '1':
        ora_exp(curs)
    elif incont == '0':
        Choice.choice(curs)
    else:
        return True
