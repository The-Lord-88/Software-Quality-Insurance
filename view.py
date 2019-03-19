from tkinter import StringVar, Label, Button, N, S, E, W, font
from model import Model
from controller import Controller

class View:
    def __init__(self, master):
        self.master = master
        self.model = Model()
        self.controller = Controller(self.model)
        master.title("Calculator")
        self.master.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.master.columnconfigure((0, 1, 2, 3), weight=1)

        self.display = StringVar()

        self.display_label = Label(master, anchor=E, textvariable=self.display, font=(None, 48))
        self.display_label.grid(columnspan=4, sticky=E+W)

        # Row 1

        self.clear_entry_button = Button(master, text="CE", command= lambda: self.click_handler("CE"))
        self.clear_entry_button.grid(row=1, sticky=N+S+E+W)

        self.clear_button = Button(master, text="C", command= lambda: self.click_handler("C"))
        self.clear_button.grid(row=1, column=1, sticky=N+S+E+W)

        self.delete_button = Button(master, text="⌫", command= lambda: self.click_handler("Del"))
        self.delete_button.grid(row=1, column=2, sticky=N+S+E+W)

        self.division_button = Button(master, text="÷", command= lambda: self.click_handler("/"))
        self.division_button.grid(row=1, column=3, sticky=N+S+E+W)

        # Row 2

        self.digit7_button = Button(master, text="7", command= lambda: self.click_handler("7"))
        self.digit7_button.grid(row=2, sticky=N+S+E+W)

        self.digit8_button = Button(master, text="8", command= lambda: self.click_handler("8"))
        self.digit8_button.grid(row=2, column=1, sticky=N+S+E+W)

        self.digit9_button = Button(master, text="9", command= lambda: self.click_handler("9"))
        self.digit9_button.grid(row=2, column=2, sticky=N+S+E+W)

        self.multiplication_button = Button(master, text="×", command= lambda: self.click_handler("*"))
        self.multiplication_button.grid(row=2, column=3, sticky=N+S+E+W)

        # Row 3

        self.digit4_button = Button(master, text="4", command= lambda: self.click_handler("4"))
        self.digit4_button.grid(row=3, sticky=N+S+E+W)

        self.digit5_button = Button(master, text="5", command= lambda: self.click_handler("5"))
        self.digit5_button.grid(row=3, column=1, sticky=N+S+E+W)

        self.digit6_button = Button(master, text="6", command= lambda: self.click_handler("6"))
        self.digit6_button.grid(row=3, column=2, sticky=N+S+E+W)

        self.subtraction_button = Button(master, text="−", command= lambda: self.click_handler("-"))
        self.subtraction_button.grid(row=3, column=3, sticky=N+S+E+W)

        # Row 4

        self.digit1_button = Button(master, text="1", command= lambda: self.click_handler("1"))
        self.digit1_button.grid(row=4, sticky=N+S+E+W)

        self.digit2_button = Button(master, text="2", command= lambda: self.click_handler("2"))
        self.digit2_button.grid(row=4, column=1, sticky=N+S+E+W)

        self.digit3_button = Button(master, text="3", command= lambda: self.click_handler("3"))
        self.digit3_button.grid(row=4, column=2, sticky=N+S+E+W)

        self.addition_button = Button(master, text="+", command= lambda: self.click_handler("+"))
        self.addition_button.grid(row=4, column=3, sticky=N+S+E+W)

        # Row 5

        self.plus_minus_button = Button(master, text="±", command= lambda: self.click_handler("+/-"))
        self.plus_minus_button.grid(row=5, sticky=N+S+E+W)

        self.digit0_button = Button(master, text="0", command= lambda: self.click_handler("0"))
        self.digit0_button.grid(row=5, column=1, sticky=N+S+E+W)

        self.decimal_point_button = Button(master, text=".", command= lambda: self.click_handler("."))
        self.decimal_point_button.grid(row=5, column=2, sticky=N+S+E+W)

        self.equals_button = Button(master, text="=", command= lambda: self.click_handler("="))
        self.equals_button.grid(row=5, column=3, sticky=N+S+E+W)

        self.display.set(self.model.display)

    def click_handler(self, button_label):
        self.controller.button_pressed(button_label)
        self.display.set(self.model.display)
