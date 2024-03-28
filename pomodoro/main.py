import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "None"

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro🍅")
window.config(padx=100, pady=50,bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)




# 10-10:30
# break
# 10:40 - 11:20
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

def count_down(count):
    c_min = count//60
    c_sec = count%60
    formatted_time = f"{c_min:02d}:{c_sec:02d}"
    #
    # if c_sec == 0:
    #     c_sec = "00"
    # elif int(c_sec) < 10 :
    #     c_sec = f"0{c_sec}"
    # elif int(c_min) < 10:
    #     c_min = f"0{c_min}"
    canvas.itemconfig(timer_text,text=f"{formatted_time}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(fg=RED,text=f"Long Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(fg=PINK,text=f"Short Break")
        count_down(short_break_sec)
    else:
        title_label.config(fg=GREEN,text=f"Working ")
        count_down(work_sec)



start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1, row=3)
window.mainloop()

count = 340
c_min = count // 60
c_sec = count % 60
print(c_min, c_sec)