import tkinter as tk
from tkinter import ttk
import time
import ttkbootstrap as tb  # For CSS-like theming
import random
from itertools import cycle
import winsound  # For sound effects
from PIL import Image, ImageTk  # For handling images

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Apply Bootstrap theme (CSS-like styling)
        self.style = tb.Style("darkly")  # Options: "darkly", "cosmo", "flatly", etc.

        # Load and set the navigation bar background image
        self.nav_frame = tk.Frame(root, height=50, bg="black")
        self.nav_frame.pack(fill=tk.X)

        try:
            self.bg_image = Image.open("path/to/your/image.png")  # Replace with your image path
        
            self.bg_image = self.bg_image.resize((400, 50), Image.ANTIALIAS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self.nav_frame, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Error loading image:", e)

        # Stopwatch variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Background animation colors
        self.colors = cycle(["#ff5733", "#33ff57", "#3357ff", "#ff33a8", "#a833ff", "#ff8c33"])
        self.animate_background()

        # Stopwatch Label with glow effect
        self.stopwatch_label = ttk.Label(root, text="00:00:00", font=("Arial", 30, "bold"), bootstyle="primary")
        self.stopwatch_label.pack(pady=20)

        # Buttons with CSS-like styles
        self.start_button = tb.Button(root, text="Start", command=self.start_stopwatch, bootstyle="success-outline")
        self.start_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.stop_button = tb.Button(root, text="Stop", command=self.stop_stopwatch, bootstyle="danger-outline")
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.reset_button = tb.Button(root, text="Reset", command=self.reset_stopwatch, bootstyle="warning-outline")
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Clock Label with glow effect
        self.clock_label = ttk.Label(root, text="00:00:00", font=("Arial", 20, "bold"), bootstyle="info")
        self.clock_label.pack(pady=10)

        # Update functions
        self.update_clock()
        self.update_stopwatch()

    def animate_background(self):
        """Animate the background color."""
        next_color = next(self.colors)
        self.root.configure(bg=next_color)
        self.root.after(1000, self.animate_background)

    def update_stopwatch(self):
        """Update the stopwatch time if running."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.stopwatch_label.config(text=self.format_time(self.elapsed_time))
            self.root.after(100, self.update_stopwatch)

    def update_clock(self):
        """Update the clock every second."""
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def start_stopwatch(self):
        """Start the stopwatch."""
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            winsound.Beep(500, 200)  # Beep sound when starting
            self.update_stopwatch()

    def stop_stopwatch(self):
        """Stop the stopwatch."""
        self.running = False
        winsound.Beep(300, 200)  # Beep sound when stopping

    def reset_stopwatch(self):
        """Reset the stopwatch."""
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")
        winsound.Beep(700, 200)  # Beep sound when resetting

    def format_time(self, elapsed_time):
        """Format elapsed time in HH:MM:SS."""
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

# Main window
if __name__ == "__main__":
    root = tb.Window(themename="superhero")  # CSS-like theme
    app = StopwatchClockApp(root)
    root.mainloop()



