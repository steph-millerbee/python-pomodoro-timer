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

def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  timer_label.config(text="Timer", fg=GREEN)
  check_labels.config(text="")
  global reps
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN *60

  if reps > 8:
    reps = 0

  elif reps == 8:
    count_down(long_break_sec)
    timer_label.config(text="Long Break", fg=RED)   

  elif reps % 2 == 0:
    count_down(short_break_sec)   
    timer_label.config(text="Short Break", fg=PINK) 

  else:
    count_down(work_sec)
    timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

  count_min = math.floor(count / 60)
  count_sec = count % 60

  if count_sec < 10:
    count_sec = f"0{count_sec}"
  if count_min == 0:
    count_min = "00"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1) # method that calls a function after a denoted amount of time. takes in time in milliseconds, so 1000ms == 1 second. required args: (ms, func, *args). *args will be passed into the declared function within .after() method.
  else:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):      
      marks += "✔"
    check_labels.config(text=marks, fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # tkinter class that reads through a file and accepts the value of the image to use in the "create_image" method later on.
canvas.create_image(100, 112, image=tomato_img) # x and y values are set at half the width and height of the canvas in order to put the image right in the middle.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1) # PACK OR GRID METHOD MUST BE USED IN ORDER FOR ANYTHING TO DISPLAY

timer_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
timer_label.config(padx=20, pady=10)

start_button = Button(text="Start", bg="white", width=5, border=0, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", width=5, border=0, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_labels = Label(font=(FONT_NAME, 14), bg=YELLOW)
check_labels.grid(column=1, row=4)
check_labels.config(padx=20, pady=10)




window.mainloop()