import tkinter as tk

# === GLOBAL CONFIG ===
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# === MAIN TIMER CLASS ===
class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        # Track time
        self.remaining_time = 0
        self.timer_running = False

        # --- Mode Buttons ---
        self.mode_frame = tk.Frame(root)
        self.mode_frame.pack(pady=10)

        self.work_button = tk.Button(self.mode_frame, text="Pomodoro", command=self.start_work)
        self.work_button.grid(row=0, column=0, padx=5)

        self.short_break_button = tk.Button(self.mode_frame, text="Short Break", command=self.start_short_break)
        self.short_break_button.grid(row=0, column=1, padx=5)

        self.long_break_button = tk.Button(self.mode_frame, text="Long Break", command=self.start_long_break)
        self.long_break_button.grid(row=0, column=2, padx=5)

        # --- Timer Display ---
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        # --- Controls ---
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        self.start_button = tk.Button(self.control_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.reset_button = tk.Button(self.control_frame, text="⟳", command=self.reset_timer)
        self.reset_button.grid(row=0, column=1, padx=5)

        # You can add settings button here if you want (⚙ symbol)

    def start_work(self):
        self.set_timer(WORK_MIN * 60)

    def start_short_break(self):
        self.set_timer(SHORT_BREAK_MIN * 60)

    def start_long_break(self):
        self.set_timer(LONG_BREAK_MIN * 60)

    def set_timer(self, seconds):
        self.remaining_time = seconds
        self.update_display()

    def start_timer(self):
        if not self.timer_running and self.remaining_time > 0:
            self.timer_running = True
            self.countdown()

    def countdown(self):
        if self.remaining_time > 0 and self.timer_running:
            mins, secs = divmod(self.remaining_time, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.timer_label.config(text="00:00")
            self.timer_running = False
            # Optionally add sound or popup here
            print("⏰ Time's up!")

    def reset_timer(self):
        self.timer_running = False
        self.remaining_time = WORK_MIN * 60
        self.update_display()

    def update_display(self):
        mins, secs = divmod(self.remaining_time, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
