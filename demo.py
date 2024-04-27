import tkinter as tk
import time

def start_timer():
    global remaining_time
    try:
        minutes = int(entry.get())
        remaining_time = minutes * 60  # Convert minutes to seconds
        update_timer()
    except ValueError:
        print("Please enter a valid integer.")

def update_timer():
    global remaining_time
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        timer_label.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

# Create the main window
root = tk.Tk()
root.title("Timer")

# Create an Entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

# Create a label to display the timer
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
timer_label.pack(pady=10)

root.mainloop()
