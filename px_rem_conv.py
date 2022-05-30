from tkinter import *

tk = Tk()

#px -> rem 변환 프로그램 
#창 설정
tk.title('PX to REM converter')
tk.geometry("340x50+100+100")
tk.resizable(0,0)

# 입력단 만들기
entry1=Entry()
entry2=Entry()
#입력단 위치설정
entry1.grid(row=0,column=1)
entry2.grid(row=0,column=3)
label1=Label(text='px').grid(row=0,column=0)
lboel2=Label(text='rem').grid(row=0,column=2)

def px_rem():
    px = entry1.get()
    entry2.delete(0,'end')
    entry2.insert(0,round(float(px)/16,2))

def rem_px():
    rem = entry2.get()
    entry1.delete(0,'end')
    entry1.insert(0,round(float(rem)*16,2))
#버튼 설정
bt1 = Button(tk,text='px->rem',bg='black',fg='white',command=px_rem).grid(row=2,column=1)
bt2 = Button(tk,text='px->rem',bg='black',fg='white',command=rem_px).grid(row=2,column=3)

tk.mainloop()