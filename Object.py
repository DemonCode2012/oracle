import Choice


def ora_object(curs, conn):
    ownnm = input("请输入用户名：")

    dictype = """select rownum, object_type from 
    (select object_type,count(*) from dba_objects 
    where owner='{}'
    group by object_type order by count(*) desc)
    order by 1""".format(ownnm.upper())
    rr = curs.execute(dictype)
    dicttp = {}
    for result in rr:
        rownum = result[0]
        objtype = result[1]
        dicttp[rownum] = objtype
    try:
        for i in range(1, len(dicttp)+1):
            print('{}.{}'.format(i, dicttp[i]))
    except KeyError:
        print('\n')

    objtp = input("请输入上述一种对象类型的编号：")

    count = 0
    while count < 3:
        if objtp == '':
            if count == 0:
                objtp = input("请重新输入上述一种对象类型的编号：")
                count += 1
            elif count == 1:
                objtp = input("请认真输入上述一种对象类型的编号：")
                count += 1
            else:
                print("再见！")
                exit()
        else:
            break

    try:
        obj = """select object_id,data_object_id,object_name,object_type,status,
        to_char(created,'yyyymmdd hh24:mi:ss'),
        to_char(LAST_DDL_TIME,'yyyymmdd hh24:mi:ss')
        from dba_objects
        where owner='{0}'
        and object_type='{1}'
        order by object_id,object_name""".format(ownnm.upper(), dicttp[eval(objtp)])
        rr = curs.execute(obj)
        for result in rr:
            objid = result[0]
            dobjid = result[1]
            objnm = result[2]
            stat = result[3]
            created = result[4]
            ddltm = result[5]
            print('{0}的{4}对象{3}编号为{1},DATA_ID为{2}创建于{6},最后一次ddl的时间是{7}.'.format(ownnm, objid, dobjid, objnm,
                                                                                dicttp[eval(objtp)], stat, created,
                                                                                ddltm))
    except KeyError:
        print('\n')

    incont = input("是否继续查询用户对象：（输入1继续,输入0返回上一菜单,其他输入退出）")
    if incont == '1':
        ora_object(curs, conn)
    elif incont == '0':
        Choice.choice(curs, conn)
    else:
        return True
