"""/*
 * @Author: Pierre Loneux 
 * @Date: 2019-03-19 19:40:36 
 * @Last Modified by:   Pierre Loneux 
 * @Last Modified time: 2019-03-19 19:40:36 
 */"""

class Controller:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operators = ["+", "-", "*", "/"]

    def __init__(self, model):
        self.model = model
        self.operand1 = "0"
        self.operand2 = ""
        self.operator = ""
        self.last_operand2 = ""
        self.last_operator = ""

    # We check if the user is typing the 1st/2nd operand or the operator, then we reset it
    def clear_entry(self):
        if self.operand1 != "0" and self.operand2 == "" and self.operator == "":
            self.operand1 = "0"
            self.model.display = self.operand1
        elif self.operator != "" and self.operand2 == "":
            self.operator = ""
            self.model.display = self.operator
        else:
            self.operand2 = "0"
            self.model.display = self.operand2

    # We just reset everything
    def clear(self):
        self.operand1 = "0"
        self.operand2 = ""
        self.operator = ""
        self.last_operand2 = ""
        self.last_operator = ""
        self.model.display = self.operand1

    # We find out which operand is currently being modified, then we remove the last number
    def delete(self):
        if self.operand2 == "" and self.operator == "":
            self.operand1 = self.operand1[:-1]
            if not self.operand1:
                self.operand1 = "0"
            self.model.display = self.operand1
        elif self.operator != "" and self.operand2 != "":
            self.operand2 = self.operand2[:-1]
            if not self.operand2:
                self.operand2 = "0"
            self.model.display = self.operand2

    def addition(self):
        self.operand1 = str(float(self.operand1) 
                        + float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def substraction(self):
        self.operand1 = str(float(self.operand1)
                        - float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def multiplication(self):
        self.operand1 = str(float(self.operand1)
                        * float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    # We just check if there is no division by 0
    def division(self):
        if self.operand2 == "0":
            self.operand1 = "Division by 0"
        else:
            self.operand1 = str(float(self.operand1)
                            / float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    # We check if the number is negative, if it is then we remove the '-' sign
    # If it is not, then we simply add it
    def plus_minus(self):
        if self.operand2 == "" and self.operator == "":
            if self.operand1[0] == '-':
                self.operand1 = self.operand1[1:]
            elif self.operand1 != "0":
                self.operand1 = "-" + self.operand1
            self.model.display = self.operand1
        else:
            if self.operand2 == "":
                self.operand2 = self.operand1
            if self.operand2[0] == '-':
                self.operand2 = self.operand2[1:]
            elif self.operand2 != "0":
                self.operand2 = "-" + self.operand2
            self.model.display = self.operand2

    # We check if the number is already a float, if it is not then we add a '.'
    def add_float(self):
        if self.operand2 == "":
            if "." not in self.operand1:
                self.operand1 += "."
            self.model.display = self.operand1
        else:
            if "." not in self.operand2:
                self.operand2 += "."
            self.model.display = self.operand2

    # Here we just save the last operands and operator used (if any), then we perform the calculation
    def calculate(self):
        if self.operand2 != "":
            self.last_operand2 = self.operand2
        if self.operator != "":
            self.last_operator = self.operator
        if self.operator != "" and self.operand2 == "":
            self.last_operand2 = self.operand1

        if self.last_operator != "":
            self.operator = self.last_operator
            if self.last_operand2 != "":
                self.operand2 = self.last_operand2
            else:
                self.operand2 = self.operand1
            if self.operator == "+":
                self.addition()
            if self.operator == "-":
                self.substraction()
            if self.operator == "*":
                self.multiplication()
            if self.operator == "/":
                self.division()

    # Here we store the user input in the matching operand/operator variable
    def store_input(self, button_label):
        if button_label in self.numbers:
            if self.operator == "":
                if self.operand1 == "0":
                    self.operand1 = button_label
                else:
                    self.operand1 += button_label
            else:
                if self.operand2 == "0":
                    self.operand2 = button_label
                else:
                    self.operand2 += button_label
        elif button_label in self.operators:
            self.operator = button_label

    #This method is used to refresh the display when a new number is entered
    def display_number(self):
        if self.operand2 == "" and self.operator == "":
            self.model.display = self.operand1
        elif self.operand2 == "" and self.operator != "":
            self.model.display = self.operator
        elif self.operand2 != "" and self.operator != "":
            self.model.display = self.operand2

    # This is called everytime a button is pressed
    # We just redirect to the correct function based on the user input
    def button_pressed(self, button_label):
        if self.operand1 == "Division by 0":
            self.operand1 = "0"
            self.operand2 = ""
            self.operator = ""

        self.store_input(button_label)

        if button_label == "CE":
            self.clear_entry()
        if button_label == "C":
            self.clear()
        if button_label == "Del":
            self.delete()
        if button_label == "+/-":
            self.plus_minus()
        if button_label == ".":
            self.add_float()
        if button_label == "=":
            self.calculate()
        else:
            self.display_number()
