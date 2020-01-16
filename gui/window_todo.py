import tkinter as tk

from gui import window_choice as choice


def f_todowin(curs):
    todowin = tk.Tk()
    todowin.title('OracleInfo')
    todowin.geometry('500x300')
    maintext = tk.Label(todowin, text='请选择你要查询你的信息：\n(输入序号即可,输入非序号输出)', font=('黑体', 18))
    maintext.pack()

    # #########    Radiobutton    ######### #
    def print_selection():
        v = var.get()

        # v = 1
        if v == 0:
            print('nothing get')
        else:
            print('您选择了', v)
            print('Selecting ...')
            choice.choice(curs, v)
            if choice.choice(curs, v):
                print('Selected !')
                todowin.destroy()
        return v

    var = tk.IntVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
    tk.Radiobutton(todowin, text='1.表空间数据文件'.ljust(100), variable=var, value=1,
                   indicatoron=0, command=print_selection).place(x=50, y=60)
    tk.Radiobutton(todowin, text='2.用户'.ljust(115), variable=var, value='2',
                   indicatoron=0, command=print_selection).place(x=50, y=90)
    tk.Radiobutton(todowin, text='3.用户对象'.ljust(109), variable=var, value='3',
                   indicatoron=0, command=print_selection).place(x=50, y=120)
    tk.Radiobutton(todowin, text='8.查看执行计划'.ljust(103), variable=var, value='8',
                   indicatoron=0, command=print_selection).place(x=50, y=150)
    tk.Radiobutton(todowin, text='10.导出表数据为csv'.ljust(99), variable=var, value='10',
                   indicatoron=0, command=print_selection).place(x=50, y=180)
    return var.get()
