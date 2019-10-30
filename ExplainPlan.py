import Choice


def plan_cursor(curs, sqlid):
    sqlplan = "select * from table(dbms_xplan.display_cursor('{}',null,'advanced'))".format(sqlid)
    rr = curs.execute(sqlplan)
    for result in rr:
        result = ''.join(result)
        if result[-16:] == 'cannot be found ':
            print("CURSOR中获取不到执行计划")
            break
        if result != ' ':
            print(result)


def plan_awr(curs, sqlid):
    sqlplan = "select * from table(dbms_xplan.display_awr('{}',null,null,'all'))".format(sqlid)
    rr = curs.execute(sqlplan)
    for result in rr:
        if curs.getCount() == 0:
            print("AWR中获取不到执行计划")
        else:
            result = ''.join(result)
            if result != ' ':
                print(result)


def getplan(curs):
    # sqlid = input("请输入已知的SQL_ID：")
    sqlid = 'gg5uc5xbf58j2'
    display = input('请选择：1.cursor 2.awr')
    if display == '1':
        plan_cursor(curs, sqlid)
    elif display == '2':
        plan_awr(curs, sqlid)
    else:
        getplan(curs)

    incont = input("是否继续查询用户对象：（输入1继续,输入0返回上一菜单,其他输入退出）")
    if incont == '1':
        getplan(curs)
    elif incont == '0':
        Choice.choice(curs)
    else:
        return True