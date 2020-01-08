import tkinter as tk
todowin = tk.Tk()

todowin.title('OracleInfo')
todowin.geometry('500x300')
maintext = tk.Label(todowin, text='Please Choose what you want to know', font=('黑体', 18))
maintext.pack()

feature = tk.Listbox(todowin)
feature.pack()

for item in ['1', '2', '3', '4']:
    feature.insert('end', item)

# btn_back = tk.Button(mainwin, text='Back', command=usr_login)
# btn_exit = tk.Button(mainwin, text='Exit', command=usr_login)
# btn_select = tk.Button(mainwin, text='Select', command=usr_login)

todowin.mainloop()
