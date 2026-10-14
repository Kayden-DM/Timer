import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

time_left = 0
running = False


def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def add_time(amount):
    global time_left
    if running:
        return
    time_left = max(0, time_left + amount)
    time_label.configure(text=format_time(time_left))


def start():
    global running
    if running or time_left <= 0:
        return
    running = True
    pause_btn.configure(text="Pause")
    tick()


def tick():
    global time_left, running
    if not running:
        return
    if time_left > 0:
        time_left -= 1
        time_label.configure(text=format_time(time_left))
        root.after(1000, tick)
    else:
        running = False
        time_label.configure(text="Time's up!")
        pause_btn.configure(text="Pause")


def pause():
    global running
    if running:
        running = False
        pause_btn.configure(text="Resume")
    elif time_left > 0:
        running = True
        pause_btn.configure(text="Pause")
        tick()


def reset():
    global time_left, running
    time_left = 0
    running = False
    time_label.configure(text=format_time(time_left))
    pause_btn.configure(text="Pause")


root = ctk.CTk()
root.title("Timer")
root.geometry("800x400")

time_label = ctk.CTkLabel(root, text="00:00", font=("Arial", 50))
time_label.pack(pady=30)

button_row = ctk.CTkFrame(root)
button_row.pack(pady=10)

ctk.CTkButton(button_row, text="+1 sec",   font=("Arial", 16), width=80, command=lambda: add_time(1)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+10 secs", font=("Arial", 16), width=80, command=lambda: add_time(10)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+30 secs", font=("Arial", 16), width=80, command=lambda: add_time(30)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+1 min",   font=("Arial", 16), width=80, command=lambda: add_time(60)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+5 mins",  font=("Arial", 16), width=80, command=lambda: add_time(300)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+10 mins", font=("Arial", 16), width=80, command=lambda: add_time(600)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+30 mins", font=("Arial", 16), width=80, command=lambda: add_time(1800)).pack(side="left", padx=3)
ctk.CTkButton(button_row, text="+1 hour",  font=("Arial", 16), width=80, command=lambda: add_time(3600)).pack(side="left", padx=3)

button_row2 = ctk.CTkFrame(root)
button_row2.pack(pady=10)

ctk.CTkButton(button_row2, text="-1 sec",   font=("Arial", 16), width=80, command=lambda: add_time(-1)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-10 secs", font=("Arial", 16), width=80, command=lambda: add_time(-10)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-30 secs", font=("Arial", 16), width=80, command=lambda: add_time(-30)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-1 min",   font=("Arial", 16), width=80, command=lambda: add_time(-60)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-5 mins",  font=("Arial", 16), width=80, command=lambda: add_time(-300)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-10 mins", font=("Arial", 16), width=80, command=lambda: add_time(-600)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-30 mins", font=("Arial", 16), width=80, command=lambda: add_time(-1800)).pack(side="left", padx=3)
ctk.CTkButton(button_row2, text="-1 hour",  font=("Arial", 16), width=80, command=lambda: add_time(-3600)).pack(side="left", padx=3)

control_row = ctk.CTkFrame(root)
control_row.pack(pady=30)

ctk.CTkButton(control_row, text="Start", font=("Arial", 20), width=100, command=start).pack(side="left", padx=5)

pause_btn = ctk.CTkButton(control_row, text="Pause", font=("Arial", 20), width=100, command=pause)
pause_btn.pack(side="left", padx=5)

ctk.CTkButton(control_row, text="Reset", font=("Arial", 20), width=100, command=reset).pack(side="left", padx=5)

root.mainloop()