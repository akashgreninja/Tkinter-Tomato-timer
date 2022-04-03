from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    my_button_1.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1
    word_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*30
    count_down(5*60)


    if reps%8==0:
        count_down(long_break_sec)
        my_label_1.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        my_label_1.config(text="Break", fg=PINK)
    else:
        count_down(word_sec)
        my_label_1.config(text="Work", fg=GREEN)
        # checkmark.config(text="✓",fg=GREEN)







# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    # if count_sec <0:
    #     count_sec=f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000 ,count_down, count-1)
    else:
        work = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            work += "✓"
            checkmark.config(text=work, fg=GREEN)
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
# window.after()




my_label_1=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"))
my_label_1.grid(column=1,row=0)

my_button_1=Button(text="Start",fg=GREEN,highlightthickness=0,command=start_timer)
my_button_1.grid(column=0,row=3)

my_button_2=Button(text="Reset",fg=GREEN,highlightthickness=0,command=reset_timer)
my_button_2.grid(column=3,row=3)


checkmark=Label(text="",fg=GREEN,font=(FONT_NAME,20,"bold"))
checkmark.grid(column=1,row=4)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_war=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_war)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#

window.mainloop()


# def timer(count):
#     if count > 0:
#         print(count)
#
#     count-=1
#     timer(count)
#
#
# timer(20)
