from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#159B26"
GREY = "#9D9B97"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

TICK = "✔"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

reps = 0
label_counter = 0

timer = None


# --------------------------- TIMER RESET ------------------------------- #
def reset_button_command():
    global reps, label_counter, timer
    reps = 0
    label_counter = 0
    # Heading Label Reset
    heading_label.config(text="Pomodoro App")
    heading_label.place(x=30, y=30)
    # Canvas Reset
    canvas.itemconfig(timer_text, text="00:00")
    # Timer reset
    window.after_cancel(timer)
    # Reset tick and break labels color to grey
    for item in labels_list:
        item.config(fg=GREY)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_command():
    time = None
    global reps, heading_text, x_head_cor, y_head_cor
    if reps % 2 == 0:
        # work time
        heading_text = "Work Time"
        x_head_cor = 75
        y_head_cor = 17
        time = WORK_MIN * 60
    elif reps % 2 != 0 and reps != 7:
        # Short Break
        heading_text = "Short break"
        x_head_cor = 47
        y_head_cor = 17
        time = SHORT_BREAK_MIN * 60
    elif reps == 7:
        # Long Break
        heading_text = "Long break"
        x_head_cor = 60
        y_head_cor = 17
        time = LONG_BREAK_MIN * 60
    heading_label.config(text=heading_text)
    heading_label.place(x=x_head_cor, y=y_head_cor)
    reps += 1
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min_text = math.floor(count / 60)
    sec_text = count % 60
    if min_text < 10:
        min_text = f"0{min_text}"
    if sec_text < 10:
        sec_text = f"0{sec_text}"
    screen_text = f"{min_text}:{sec_text}"
    if count >= 0:
        canvas.itemconfig(timer_text, text=screen_text)
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        global label_counter
        labels_list[label_counter].config(fg=GREEN)
        label_counter += 1
        start_button_command()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.minsize(width=400, height=400)
window.config(bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.place(x=100, y=80)

# LABEL (TIMER OR BREAK)
heading_text = "Pomodoro App"
x_head_cor = 30
y_head_cor = 30
heading_label = Label(text=heading_text, font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
heading_label.place(x=30, y=30)

# LABEL (Tick Marks)
tick_label_1 = Label(text=TICK, fg=GREY, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
tick_label_1.place(x=110, y=310)

tick_label_2 = Label(text=TICK, fg=GREY, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
tick_label_2.place(x=155, y=310)

tick_label_3 = Label(text=TICK, fg=GREY, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
tick_label_3.place(x=200, y=310)

tick_label_4 = Label(text=TICK, fg=GREY, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
tick_label_4.place(x=245, y=310)

# break labels
break_label_1 = Label(text="🅑", font=(FONT_NAME, 20, "normal"), fg=GREY, bg=YELLOW)
break_label_1.place(x=130, y=330)

break_label_2 = Label(text="🅑", font=(FONT_NAME, 20, "normal"), fg=GREY, bg=YELLOW)
break_label_2.place(x=175, y=330)

break_label_3 = Label(text="🅑", font=(FONT_NAME, 20, "normal"), fg=GREY, bg=YELLOW)
break_label_3.place(x=220, y=330)

long_label = Label(text="👍", font=(FONT_NAME, 18, "normal"), fg=GREY, bg=YELLOW)
long_label.place(x=265, y=330)

# list of tick marks
labels_list = [tick_label_1, break_label_1, tick_label_2, break_label_2, tick_label_3, break_label_3, tick_label_4,
               long_label]

# Buttons (start and reset)
start_button = Button(text="Start", highlightthickness=0, command=start_button_command)
start_button.place(x=30, y=315)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_button_command)
reset_button.place(x=310, y=315)

window.mainloop()
