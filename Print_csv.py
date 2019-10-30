import os
import csv
import datetime


def print_csv(curs, tbnm, printsql, count):
    start_time = datetime.datetime.now()
    # output each table content to a separate CSV file
    # filepath =
    print("当前路径：{}".format(os.getcwd()))
    filepath = input("请输入路径：输入为空则使用上述当前路径")
    if filepath == '':
        filepath = os.getcwd()
    else:
        if not os.path.isdir(filepath):
            os.makedirs(filepath)
        else:
            os.chdir(filepath)
    print("修改后路径：{}".format(filepath))

    rr = curs.execute(printsql)

    interval = eval(input("请输入每个文件存放的行数:"))

    if count[0] < interval:
        csv_file_dest = tbnm + ".csv"
        if os.path.isfile(csv_file_dest):
            ifdel = input('是否覆盖重命名文件(y/n:)')
            if ifdel in ['y', 'yes', 'YES', 'Y']:
                os.remove(csv_file_dest)
            else:
                filename = input("请输入新的文件名")
                if filename == '':
                    print('新文件名为空，可以输出结果但是可能无法打开，请先从系统中重命名后再次打开。')
                csv_file_dest = filename + '.csv'
        print("Starting Printing to csv ... \n Path : {0}//{1}".format(filepath, csv_file_dest))
        outputfile = open(csv_file_dest, 'w', newline='')  # 'wb'
        output = csv.writer(outputfile, dialect='excel')
        # add column headers if requested
        cols = []
        for col in curs.description:
            cols.append(col[0])
        output.writerow(cols)
        for row_data in curs:  # add table rows
            output.writerow(row_data)
    else:
        for i in range(1, (count[0]//interval)+2):
            csv_file_dest = tbnm + '-' + str(i) + ".csv"
            if os.path.isfile(csv_file_dest):
                ifdel = input('是否覆盖重命名文件(y/n:)')
                if ifdel in ['y', 'yes', 'YES', 'Y']:
                    os.remove(csv_file_dest)
                else:
                    filename = input("请输入新的文件名")
                    if filename == '':
                        print('新文件名为空，可以输出结果但是可能无法打开，请先从系统中重命名后再次打开。')
                    csv_file_dest = filename + '-' + str(i) + ".csv"
            print("Starting Printing to csv ... \n Path : {0}//{1}".format(filepath, csv_file_dest))
            outputfile = open(csv_file_dest, 'w', newline='')  # 'wb'
            output = csv.writer(outputfile, dialect='excel')
            # add column headers if requested
            cols = []
            for col in curs.description:
                cols.append(col[0])
            output.writerow(cols)
            if i == (count[0]//interval)+1:
                for row_data in rr.fetchall():  # add table rows
                    output.writerow(row_data)
            else:
                for row_data in rr.fetchmany(numRows=interval):  # add table rows
                    output.writerow(row_data)
            outputfile.close()

    end_time = datetime.datetime.now()
    interval = (end_time - start_time).seconds
    if interval > 60:
        final_time = interval / 60.0
        print("Print to CSV complete success! \n Time : {:2f} min".format(final_time))
    else:
        print("Print to CSV complete success! \n Time : {:2f} s".format(interval))
