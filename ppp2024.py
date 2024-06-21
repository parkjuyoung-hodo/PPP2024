from tkinter import * #창 생성하기 위해 칠수
import tkinter as tk
import tkinter.ttk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import webbrowser
import os.path
import pandas as pd
from tkinter import messagebox
from openpyxl import load_workbook
from datetime import datetime

def add_project():
    project_name=project_entry.get()
    schedule = schedule_entry.get_date()
    # project_manager =manager_entry.get()
    table.insert('','end',values=(project_name,schedule))


win=Tk() #창 생성하기 위해 필수

#창크기
win.geometry("500x700")

#창제목
win.title("도파민 중독 방지 프로그램")

#전체 폰트
win.option_add('*FONT','맑은고딕25')
#Notebook 사용
notebook =tkinter.ttk.Notebook(win, width=500, height=700)
notebook.pack()

# 첫 번쨰 장
frame_1 =tkinter.Frame(win)
notebook.add(frame_1,text='할 일 적기')

frame_1=tkinter.Label(frame_1, text="해야 할 일")
frame_1.pack()

project_label =ttk.Label(frame_1, text='프로젝트명')  #이거 from tkinter import ttk 이 코드를 필요로 함
project_label.pack()
project_entry =ttk.Entry(frame_1) #이걸 Entry()에 열 창을 입력하면 됩니다
project_entry.pack()

schedule_label =ttk.Label(frame_1, text='일정')
schedule_label.pack()
schedule_entry =DateEntry(frame_1)
schedule_entry.pack()


add_button =tk.Button(frame_1,text='프로젝트 추가',command=add_project)
add_button.pack()

table=ttk.Treeview(frame_1,columns=('프로젝트명','일정'),show='headings')
table.heading('프로젝트명',text='프로젝트명')
table.heading('일정',text='일정')
# table.heading('기타사항',text='기타사항')
table.pack()



#두 번쨰 장
frame2=tk.Frame(win)
notebook.add(frame2, text="유튜브 접속")

label1=tk.Label(frame2, text="오늘 꼭 해야 하는 일은?")
label1.pack()

ent_label1 =tk.Entry(frame2, width=100)
ent_label1.insert(0, "유튜브를 보고 싶으면 작성하시오")


def clear(event):
    if ent_label1.get() == "유튜브를 보고 싶으면 작성하시오":
        ent_label1.delete(0,len(ent_label2.get()))


ent_label1.bind('<Button-1>',clear) # Button-1 (마우스 좌클릭) 이벤트 발생 시 clear 함수 실행
ent_label1.pack()
def clear(event):
    ent_label1.delete()

label2= Label(frame2)
label2.config(text="만약 그 일을 하지 않는다면?")
label2.pack()

ent_label2 =Entry(frame2,width=100)
ent_label2.pack()

label3= Label(frame2)
label3.config(text="유튜브를 지금 보면 좋은 점은?")
label3.pack()

ent_label3 =Entry(frame2,width=100)
ent_label3.pack()


label4 = ttk.Label(frame2,text='위험: 바이러스 위험이 있는 유튜브를 실행할 것 인가요??!?',width=100)
label4.pack()

ent_label4 = ttk.Combobox(frame2,values=["yes",'예'],width=100)
ent_label4.pack()

def btn_exit():
    q1 = str(ent_label1.get())
    q2 = str(ent_label2.get())
    q3 = str(ent_label3.get())
    q4 = str(ent_label4.get())


    if q1 == "":
        tk.messagebox.showerror("확인", '"오늘 꼭 해야 하는 일은?"질문을 대답해주세요!')
        ent_label1.focus()
        return
    if q2 == "":
        tk.messagebox.showerror("확인", '"만약 그 일을 하지 않는다면?"질문을 대답해주세요!')
        ent_label2.focus()
        return

    if q3 == "":
        tk.messagebox.showerror("확인", '"유튜브를 지금 보면 좋은 점은?"질문을 대답해주세요!')
        ent_label3.focus()
        return

    if q4 == "":
        tk.messagebox.showerror("확인", '"바이러스 위험이 있는 유튜브를 실행할 것인가요?"질문에 답해주세요!')
        ent_label4.focus()
        return

    msgbox = tk.messagebox.askquestion('확인', '유튜브를 실행하시겠습니까?')
    if msgbox == 'yes':
        open_browser()

def open_browser():
    webbrowser.open_new('https://www.youtube.com/')


youtube_button = tk.Button(frame2, text="유튜브 접속", command=btn_exit, width=10, height=2)
youtube_button.pack(pady=50)



# #세 번째 장
# frame3=tkinter.Frame(win)
# notebook.add(frame3, text="유튜브")
#
# label3=tkinter.Label(frame3, text="유튜브")
# label3.pack()


#창실행
win.mainloop()



