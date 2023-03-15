import os, csv
import re
import tkinter as tk
import tkinter.messagebox as msbox
import socket

# 默认用户
with open('data.csv', 'w') as f:
    xie = csv.writer(f)
    xie.writerow(["admin", 1234])


# 建立vip功能

# 建立函数
def system():
    '''模拟cmd输入指令,并建立对话框,上面显示着密码'''
    system_info = os.popen(f'netsh wlan show profile name={Entry.get()} key=clear').read()
    try:
        password = re.findall('关键内容:         (.*)', system_info)[0]
    except IndexError:
        msbox.showerror('Error', 'wifi账号输入错误，无法破解')
    else:
        msbox.showinfo('破解成功', f'wifi"{Entry.get()}"的密码是"{password}"')


def wifi():
    # 建立窗口
    root = tk.Tk()
    root.geometry('250x80+400+200')
    root.title('破解wifi密码')
    root.iconbitmap('./favicon.ico')
    # 建立标签
    # tk.Label(root,text='不好意思，此窗口之后可能有个黑洞洞的窗口\n但没这个窗口无法运行，请您谅解').pack()
    tk.Label(root, text='请输入wifi名称').grid()
    # 设置文本
    global Entry
    Entry = tk.Entry(root, width=23)
    Entry.grid(row=0, column=1)

    # 建立按钮ok
    ok = tk.Button(root, text='ok', command=system)
    ok.grid(row=2, column=0, sticky=tk.W)
    exit_gabaichen = tk.Button(root, text='exit', command=root.quit)
    exit_gabaichen.grid(row=2, column=1, sticky=tk.E)
    # 窗口进入消息循环
    root.mainloop()
    '''TP-LINK_C302'''


def my_if():
    # 判断用户登录
    with open('data.csv', 'r') as f:
        c = csv.reader(f)
        global list
        list = []
        for i in c:
            print(i)
            list.append(i)
        global x
        x = 0
        try:
            for i in range(len(list)):
                if Entry_0.get() in list[x]:
                    if str(Entry1.get()) == str(list[x][1]):
                        raise
                x += 1
            raise
        except:
            print('len(list)-1=' + str(len(list) - 1), 'x=' + str(x))
            if x > int(len(list)) - 1:
                msbox.showerror('Error', '账号或密码错误')
            else:
                wifi()


def new_user_hou():
    with open('data.csv', 'r', newline='') as f:
        c = csv.reader(f)
        global list
        list = []
        for i in c:
            print(i)
            list.append(i)
    with open('data.csv', 'w', newline='') as f:
        xie = csv.writer(f)
        for i in list:
            xie.writerow(i)
        xie.writerow([Entry_new_uers.get(), Entry_new_passwork.get()])


def new_user_qian():
    uers_new = tk.Tk()
    uers_new.geometry('283x80+400+200')
    uers_new.title('注册')
    uers_new.iconbitmap('./favicon.ico')
    # 建立标签
    # tk.Label(root,text='不好意思，此窗口之后可能有个黑洞洞的窗口\n但没这个窗口无法运行，请您谅解').pack()
    tk.Label(uers_new, text='请输入要注册用户名').grid(sticky=tk.W)
    # 设置文本
    global Entry_new_uers
    Entry_new_uers = tk.Entry(uers_new, width=23)
    Entry_new_uers.grid(row=0, column=1)

    tk.Label(uers_new, text='请输入要注册密码').grid(row=1, column=0, sticky=tk.W)
    # 设置文本
    global Entry_new_passwork
    Entry_new_passwork = tk.Entry(uers_new, width=23, show='*')
    Entry_new_passwork.grid(row=1, column=1)
    ok1 = tk.Button(uers_new, text='ok', command=new_user_hou)
    ok1.grid(row=2, column=0, sticky=tk.W)
    exit_gabaichen1 = tk.Button(uers_new, text='exit', command=uers_new.quit)
    exit_gabaichen1.grid(row=2, column=1, sticky=tk.E)
    uers_new.mainloop()


def uers():
    uers = tk.Tk()
    uers.geometry('250x80+400+200')
    uers.title('登录')
    uers.iconbitmap('./favicon.ico')
    # 建立标签
    # tk.Label(root,text='不好意思，此窗口之后可能有个黑洞洞的窗口\n但没这个窗口无法运行，请您谅解').pack()
    tk.Label(uers, text='请输入用户名').grid()
    # 设置文本
    global Entry_0
    Entry_0 = tk.Entry(uers, width=23)
    Entry_0.grid(row=0, column=1)

    tk.Label(uers, text='请输入密码').grid(row=1, column=0)
    # 设置文本
    global Entry1
    Entry1 = tk.Entry(uers, width=23, show='*')
    Entry1.grid(row=1, column=1)

    ok = tk.Button(uers, text='ok', command=my_if)
    ok.grid(row=2, column=0, sticky=tk.W)
    new_uers = tk.Button(uers, text='注册', command=new_user_qian)
    new_uers.grid(row=2, column=1, sticky=tk.S)
    exit_gabaichen = tk.Button(uers, text='exit', command=uers.quit)
    exit_gabaichen.grid(row=2, column=1, sticky=tk.E)

    uers.mainloop()


if __name__ == '__main__':
    uers()
