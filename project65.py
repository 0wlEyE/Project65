import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")#ขนาด
root.resizable(False,False)
root.configure(bg="#17161b")#สีพื่นหลัง
# ^ ^ ^ ส่วนหน้าต่างที่แสดง

label_result = Label(root, width=25,height=2,text="",font=("arial",30))
label_result.pack()
# ^ ^ ^ ช่องแสดงตัวเลข

Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=100)
#  ^          ^            ^      ^         ^                                            ^              ^ 
#  ปุ่ม       ชื่อปุ่ม         ขนาดของปุ่ม       ฟอนต์                                          สี         ตำแหน่งของปุ่ม
Button(root,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037").place(x=150,y=100)
Button(root,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037").place(x=290,y=100)
Button(root,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037").place(x=430,y=100)


Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36").place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36").place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36").place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037").place(x=430,y=200)

root.mainloop()


#ปู่ม 0 อยู่ที่ x=10,y=500  width=11, height=1
#ป่ม = อยู่ที่ x=430,y=500 width=5, height=3