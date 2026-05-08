# ==========================================
# DIGITAL CLOCK USING PYTHON
# ==========================================

# Import required libraries
from tkinter import *
import time


# Create the main window
root = Tk()

# Set window title
root.title("Digital Clock")

# Set window size
root.geometry("500x200")

# Set background color
root.configure(bg="black")

# Function to update the clock
def clock():

    # Get current time in HH:MM:SS AM/PM format
    current_time = time.strftime("%I:%M:%S %p")

    # Display time on label
    clock_label.config(text=current_time)

    # Update the time every 1 second
    clock_label.after(1000, clock)


# Create label for clock
clock_label = Label( root,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="#FF3131"
)

# Place the label in center
clock_label.pack(anchor="center", pady=40)


# Run the clock function
clock()

# Keep window running
root.mainloop()