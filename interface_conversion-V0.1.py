# 本代码是为了方便接口调用时，自动生成接口请求头的三个参数
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *
import random
import hashlib


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatwidget()
        self.change()

    def creatwidget(self):
        self.label1 = Label(self, text="AppToken")
        self.label1.pack()
        v1 = StringVar()
        self.entry1 = Entry(self, textvariable=v1, width=40)
        v1.set("ZhaoShuaiA")
        self.entry1.pack()

        self.label2 = Label(self, text="AppSecret")
        self.label2.pack()
        v2 = StringVar()
        self.entry2 = Entry(self, textvariable=v2, width=40)
        v2.set("4P2nOrpBC3SjeRKEFqtPmAJLRtVmFB")
        self.entry2.pack()
        # lambda:[funcA(), funcB(), funcC()]
        self.btn1 = Button(self, text="开始转换")
        # self.btn1.bind("<Button-1>",lambda event: self.turnover())
        self.btn1.bind("<Button-1>", lambda event: [self.change(), self.turnover()])
        self.btn1.pack()

        print("---------------------------------")

    def change(self):
        # 获取文本框 的值
        self.x_qys_accesstoken = self.entry1.get()

        AppSecret = self.entry2.get()
        x_qys_timestamp = 0
        a = str(self.x_qys_accesstoken + AppSecret + "0" )
        #        print("加密前的x_qys_signature"+a)
        # x_qys_signature
        input_name = hashlib.md5()
        input_name.update(a.encode("utf-8"))
        print("md5加密-小写的32位" + (input_name.hexdigest()).lower())
        # x_qys_signature = input_name.hexdigest().lower()
        self.x_qys_signature = input_name.hexdigest().lower()

    def turnover(self):
        self.label3 = Label(self, text="x-qys-accesstoken")
        self.label3.pack()
        v3 = StringVar()
        self.entry3 = Entry(self, textvariable=v3, width=40)
        v3.set(self.x_qys_accesstoken)
        self.entry3.pack()

        self.label4 = Label(self, text="x-qys-timestamp")
        self.label4.pack()
        v4 = StringVar()
        self.entry4 = Entry(self, textvariable=v4, width=40)
        v4.set("0")
        self.entry4.pack()

        self.label5 = Label(self, text="x-qys-signature")
        self.label5.pack()
        v5 = StringVar()
        self.entry5 = Entry(self, textvariable=v5, width=40)
        v5.set(self.x_qys_signature)
        self.entry5.pack()


root = Tk()
root.geometry("350x550+10+10")
root.title("契约锁接口参数转换工具")
app = Application(master=root)
root.mainloop()

