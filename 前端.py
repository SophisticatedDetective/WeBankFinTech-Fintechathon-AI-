
import tkinter as tk
import time
import webbrowser


# 创建主窗口
window = tk.Tk()
window.title('微AI战队')
window.geometry('630x150')

# 设置下载进度条
tk.Label(window, text='Training', ).place(x=50, y=60)
canvas = tk.Canvas(window, width=465, height=22, bg="white")
canvas.place(x=110, y=60)


# 显示下载进度
def progress():
    # 填充进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数
    for i in range(x):
        n = n + 465 / x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0.02)  # 控制进度条流动的速度
    IEPath = "/usr/bin/firefox"
    webbrowser.register('IE', None, webbrowser.BackgroundBrowser(IEPath))
    webbrowser.get('IE').open('http://192.168.1.126:8080/index.html#/dashboard?job_id=201908250954493676949&role=guest&party_id=10000', new=1, autoraise=True)
    # 或者
    webbrowser.open_new_tab('http://192.168.1.126:8080/index.html#/dashboard?job_id=201908250954493676949&role=guest&party_id=10000')

    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数

    for t in range(x):
        n = n + 465 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0)  # 时间为0，即飞速清空进度条


btn_download = tk.Button(window, text='Start!', command=progress)
btn_download.place(x=465/2+50, y=105)

window.mainloop()
