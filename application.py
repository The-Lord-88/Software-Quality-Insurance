"""/*
 * @Author: Pierre Loneux 
 * @Date: 2019-03-19 19:41:31 
 * @Last Modified by:   Pierre Loneux 
 * @Last Modified time: 2019-03-20 14:38:31 
 */"""

from tkinter import Tk, font
from view import View

# Here we initiate the tkinter engine, and select a font
root = Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=24)

# We then create the window that will contain our calculator
width = 450
height = 500
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

view = View(root)

# We then add attributes to the window, and display it
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)
root.mainloop()
