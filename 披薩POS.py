import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from PIL import ImageTk, Image
#做一個def
def event1():
    global entry1       # Entry 輸入框的變數
    global label2Str    # Label1 的文字 變數
    global comboExample
    global comboExample1
    global comboExample2
    global comboExample3
    global comboExample4
    print(comboExample.current(), comboExample.get())
    t1=entry1.get()     #取得用戶所輸入的文字
    twd=float(t1)
    comStr=comboExample.get()
    if comStr=="有":
        dollar=twd*0.9
    elif comStr=="沒有":
        dollar=twd
    comStr = comboExample1.get()
    if comStr=="帕瑪森":
        dollar=(dollar+20)
    elif comStr=="double起司":
        dollar=(dollar+30)
    elif comStr=="芝心":
        dollar=(dollar+50)
    elif comStr=="厚片":
        dollar=(dollar+10)
    comStr = comboExample2.get()
    if comStr=="12吋":
        dollar=(dollar+60)
    elif comStr=="9吋":
        dollar=(dollar+20)
    elif comStr=="6吋":
        dollar=dollar*0.8
    comStr = comboExample3.get()
    if comStr=="塑膠袋":
        dollar=(dollar+5)
    elif comStr=="炸雞":
        dollar=(dollar+55)
    elif comStr=="薯星星":
        dollar=(dollar+20)
    label2Str.set(str(dollar))

win = tk.Tk()
#架設POS視窗大小
win.wm_title("披薩價格")                 # 設定抬頭名稱
win.minsize(width=200, height=300)   # 320,200
win.resizable(width=False, height=False) # 是否可以改變視窗大小
#架設背景
background_image = ImageTk.PhotoImage(Image.open("bg1.jpg"))
background_label = tk.Label(win, image=background_image)
background_label.place(x=0,y=0)
#架設輸入金額
label1=tk.Label(win,text="現金:")
label1.place(x=0,y=0)
#架設輸入框
entry1=tk.Entry(win)
entry1.place(x=30,y=0)
#架設(售價)
label3=tk.Label(win,text="售價:")
label3.place(x=0,y=250)
label2Str=StringVar()
label2=tk.Label(win,text="售價",textvariable=label2Str)
label2.place(x=40,y=250) #印出選單的內容
label2Str.set("...")
#設置按鈕
img = ImageTk.PhotoImage(Image.open("button.png"))
btn1 =tk.Button(win,text="press me",image=img,command=event1)
btn1.place(x=20,y=200)

#下拉式選單(會員)
labelVip=tk.Label(win,text="會員選擇")
labelVip.place(x=0,y=40)
comboExample = ttk.Combobox(win,values=["---會員---","有","沒有"],width=8)
comboExample.place(x=60,y=40)
comboExample.current(0)  #選單的初始顯示
#下拉式選單(餅皮)
labelPie=tk.Label(win,text="餅皮選擇")
labelPie.place(x=0,y=70)
comboExample1 = ttk.Combobox(win,values=["---餅皮---","帕瑪森","double起司","芝心","厚片"],width=10)
comboExample1.place(x=60,y=70)
comboExample1.current(0)  #選單的初始顯示
#下拉式選單(尺寸)
labelSize=tk.Label(win,text="尺寸選擇")
labelSize.place(x=0,y=100)
comboExample2 = ttk.Combobox(win,values=["---尺寸---","12吋","9吋","6吋"],width=8)
comboExample2.place(x=60,y=100)
comboExample2.current(0)  #選單的初始顯示
#下拉式選單(加購)
labelAdd=tk.Label(win,text="加購選擇")
labelAdd.place(x=0,y=130)
comboExample3 = ttk.Combobox(win,values=["---加購---","塑膠袋","炸雞","薯星星"],width=8)
comboExample3.place(x=60,y=130)
comboExample3.current(0)  #選單的初始顯示
#下拉式選單(發票)
labeltax=tk.Label(win,text="發票選擇")
labeltax.place(x=0,y=160)
comboExample4 = ttk.Combobox(win,values=["---發票---","有","沒有"],width=8)
comboExample4.place(x=60,y=160)
comboExample4.current(0)  #選單的初始顯示



win.mainloop()