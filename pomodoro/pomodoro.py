from string import printable
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    reps = 0
    windows.after_cancel(timer)
    label.config(text="Timer",fg=PINK, bg=YELLOW)
    
    check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_call():
    global reps
    reps += 1
    if reps % 8 == 0 :
        count_down( 20 * 60 )
        label.config(text="Break",fg=RED)
    elif  reps % 2 == 0 :
        count_down( 5 * 60  )
        label.config(text="Break",fg=RED)
    else :
        count_down( 25 * 60)
        label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = windows.after(1000,count_down, count - 1)
    else:
        start_call()
        mark=""
        for _ in range(reps/2):
            mark += "✅"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row= 1)

label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),fg=PINK, bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0,command=start_call )
start_button.grid(column=0, row=2)

restart_button = Button(text="Reset ", highlightthickness=0, command=timer_reset)
restart_button.grid(column=2, row=2)

check = Label( font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)
windows.mainloop()