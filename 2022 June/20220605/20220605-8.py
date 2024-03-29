import time
import tkinter
import tkinter.messagebox


def download():
    # 模擬下載任務需要花費10秒鐘時間
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下載完成!')


def show_about():
    tkinter.messagebox.showinfo('關於', '作者: 陳叮(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('視窗')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下載', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='關於', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()