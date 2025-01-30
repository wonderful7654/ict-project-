
import tkinter as tk
from tkinter import Canvas
import time


# The animation function
def animate_text(root, canvas, avocado_font):
    text = "WORD"
    x, y = 400, 300  # Center of the canvas
    display_text = ""
    for char in text:
        canvas.delete("all")  # Clear canvas
        display_text += char
        canvas.create_text(
            x, y,
            text=display_text,
            font=avocado_font,
            fill="#F2F2F2",
            anchor="center"
        )
        root.update()  # Update the window
        time.sleep(0.5)  # Animation delay

    # Keep the final text on the screen
    canvas.create_text(
        x, y,
        text=text,
        font=avocado_font,
        fill="white",
        anchor="center"
    )

    # Destroy the animation window after the animation completes
    root.destroy()



