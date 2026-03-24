from tkinter import *
import time

window = Tk()
window.title("Dangerous Writing App")
window.config(padx=20, pady=20)

text_area = Text(window, width=60, height=20, font=("Arial", 12))
text_area.pack()

timer_label = Label(text="Time left: 5", font=("Arial", 14), fg="red")
timer_label.pack()

time_left = 5
timer = None


def delete_text():
    text_area.delete("1.0", END)


def countdown():
    global time_left, timer

    timer_label.config(text=f"Time left: {time_left}")
    if time_left > 0:
        time_left -= 1
        timer = window.after(1000, countdown)

    else:
        delete_text()

    if time_left <= 2:
        timer_label.config(fg="red")
    else:
        timer_label.config(fg="green")


def reset_timer(event=None):
    global timer, time_left

    if timer is not None:
        window.after_cancel(timer)

    time_left = 5
    countdown()


text_area.bind("<Key>", reset_timer)

label = Label(text="Keep typing... or your text will disappear", fg="red")
label.pack()

window.mainloop()