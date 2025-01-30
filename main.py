import tkinter as tk
import tkinter.font as font
from tkinter import Canvas
from animation import animate_text
from dictionary_app import start_dictionary_app


def main():
    #  Create the animation window
    animation_root = tk.Tk()
    animation_root.title("Word Dictionary - Animation")
    animation_root.iconbitmap(r"C:\Users\afola\Desktop\pythonprog\favicon.ico")
    animation_root.geometry("800x600")
    animation_root.configure(bg="#00008B")  # Dark blue background

    # Load the custom font
    try:
        avocado_font = font.Font(family="PlaywritePEGuides-Regular", size=100)  # Use the correct font name
    except Exception as e:
        print(f"Error loading font: {e}")
        avocado_font = font.Font(family="Arial", size=100, slant="italic")  # Fallback font

    # Create the Canvas for the animation
    canvas = Canvas(animation_root, width=800, height=600, bg="#2C2C34", highlightthickness=0)
    canvas.pack()

    
    animate_text(animation_root, canvas, avocado_font)

    
    animation_root.mainloop()

   
    start_dictionary_app()


if __name__ == "__main__":
    main()












"""         Name                         Matric
     Afolabi wonderful                 2023/12810
     Salimon Victor Abiola             2022/11216
     Alakpa Greatman                   2022/11842
     Nwanorim Micheal Chukwebuka       2022/11842   """