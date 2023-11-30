from tkinter import *
import math
import tkinter.simpledialog as simpledialog
import winsound

work_minutes = 0
break_minutes = 0
session_count = 0
timer_id = None


def reset_timer():
    start_button["state"] = "normal"
    root.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="#333333")

    global session_count
    session_count = 0


def start_timer():
    global session_count
    session_count += 1
    start_button["state"] = "disabled"
    work_seconds = work_minutes * 60
    break_seconds = break_minutes * 60

    if session_count % 2 == 0:
        count_down(break_seconds)
        title_label.config(text="Break", fg="#b885ff")
    else:
        count_down(work_seconds)
        title_label.config(text="Study/Work", fg="#2c9fa2")


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer_id
        timer_id = root.after(1000, count_down, count - 1)
    else:
        play_notification_sound()
        start_timer()


def play_notification_sound():
    sound_file = "sound.wav"
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)


def set_work_time(preset_time):
    global work_minutes, break_minutes
    work_minutes = preset_time
    break_minutes = work_minutes / 5
    start_timer()
    work_time_prompt.destroy()


def open_work_time_prompt():
    global work_time_prompt
    work_time_prompt = Toplevel(root)
    work_time_prompt.title("Set Work Time")
    work_time_prompt.config(bg="#f0f0f0")

    window_width = 280
    window_height = 120
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    work_time_prompt.geometry(
        f"{window_width}x{window_height}+{x_position}+{y_position}"
    )

    prompt_label = Label(
        work_time_prompt, text="Enter work time in minutes:", bg="#f0f0f0"
    )
    prompt_label.pack()

    work_input = Entry(work_time_prompt)
    work_input.pack()

    presets_frame = Frame(work_time_prompt, bg="#f0f0f0")
    presets_frame.pack()

    preset_10_button = Button(
        presets_frame,
        text="10 minutes",
        command=lambda: set_work_time(10),
        bg="#0fba93",
    )
    preset_10_button.pack(side=LEFT, padx=5, pady=5)

    preset_25_button = Button(
        presets_frame,
        text="25 minutes",
        command=lambda: set_work_time(25),
        bg="#0fba93",
    )
    preset_25_button.pack(side=LEFT, padx=5, pady=5)

    preset_40_button = Button(
        presets_frame,
        text="40 minutes",
        command=lambda: set_work_time(40),
        bg="#0fba93",
    )
    preset_40_button.pack(side=LEFT, padx=5, pady=5)

    submit_button = Button(
        work_time_prompt,
        text="Submit",
        command=lambda: set_work_time(int(work_input.get())),
        bg="#2c9fa2",
    )
    submit_button.pack(pady=5)


root = Tk()
root.title("Focus Tree")
root.config(bg="#f0f0f0")
img = PhotoImage(file="icon.png")
root.iconphoto(False, img)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 400
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


title_label = Label(
    text="Timer",
    fg="#333333",
    bg="#f0f0f0",
    font=("Bahnschrift SemiBold SemiConden", 50),
)
title_label.pack()

frame = Frame(root, bg="#f0f0f0")
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, width=200, height=100, highlightthickness=0, bg="#f0f0f0")
timer_text = canvas.create_text(
    100,
    50,
    text="00:00",
    fill="#333333",
    font=(
        "Bahnschrift Condensed",
        35,
    ),
)
canvas.pack()


start_button = Button(
    frame,
    text="Start",
    highlightthickness=0,
    command=open_work_time_prompt,
    bg="#2c9fa2",
    font=(
        "Bahnschrift Condensed",
        20,
    ),
)
start_button.pack(pady=10)


reset_button = Button(
    frame,
    text="Reset",
    highlightthickness=0,
    command=reset_timer,
    bg="#2c9fa2",
    font=(
        "Bahnschrift Condensed",
        20,
    ),
)
reset_button.pack(pady=10)


root.mainloop()
