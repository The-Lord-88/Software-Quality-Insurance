# Software Quality Insurance
This project aims to illustrate how software should be conceived and organized within a company.

To reach this goal, I decided to implement a calculator in Python, as it is not very complicated and the structure can be easily understood.

# Controller
This file contains the most important part of the code. This is the class that is called every time a button is pressed. Therefore, it catches the user input, and makes a call to the matching function.

# Application
This is where the main application is initiated. The project uses Tkinter for its GUI. If you are interested in this framework, you can learn more here : https://docs.python.org/3/library/tk.html

# Model
This file is only used to resfresh the display

# View
This is not a very complex part of the code. It just initiates each button that will be used in the calculator, associates it with a symbol, then sets the display.
