from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x700+100+200")#ขนาด
root.resizable(False,False)
root.configure(bg="#17161b")#สีพื่นหลัง
# ^ ^ ^ ส่วนหน้าต่างที่แสดง

equation = ""
def show(value):  # <--------- แสดงข้อมูลขึ้นจอ
    global equation
    equation += value
    label_result.config(text=equation)

def clear(): # <--------- เคลียร์ข้อมูลทั้งหมด
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
        label_result.config(text=result)

label_result = Label(root, width=25,height=2,text="",font=("arial",30))
label_result.pack()
# ^ ^ ^ ช่องแสดงตัวเลข

#------------------------------------------ ปุ่มล้วนๆ ไม่มีอย่างอื่นผสม -------------------------------------------------
Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)        # C
#  ^          ^            ^      ^         ^                                            ^              ^ 
#  ปุ่ม       ชื่อปุ่ม         ขนาดของปุ่ม       ฟอนต์                                          สี         ตำแหน่งของปุ่ม
Button(root,text="//", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("//")).place(x=150,y=100)   # //
Button(root,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("%")).place(x=290,y=100)     # %
Button(root,text="÷", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("/")).place(x=430,y=100)     # ÷


Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)      # 7
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)     # 8
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)     # 9
Button(root,text="x", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("*")).place(x=430,y=200)     # x

Button(root,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)      # 4
Button(root,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)     # 5
Button(root,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)     # 6
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("-")).place(x=430,y=300)     # -

Button(root,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)      # 1
Button(root,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)     # 2
Button(root,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)     # 3
Button(root,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: show("+")).place(x=430,y=400)     # +

Button(root,text="+/-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+/-")).place(x=10,y=500)  # +/-
Button(root,text="0", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=150,y=500)     # 0
Button(root,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)     # .
Button(root,text="=", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=500)     # =

Button(root,text="(", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("(")).place(x=10,y=600)      # (
Button(root,text=")", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(")")).place(x=150,y=600)     # )

Button(root,text="xⁿ", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("**")).place(x=290,y=600)   # xⁿ
Button(root,text="√", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("**0.5")).place(x=430,y=600)   # √
root.mainloop()


#ปู่ม 0 อยู่ที่ x=10,y=500  width=11, height=1
#ปุ่ม = อยู่ที่ x=430,y=500 width=5, height=3