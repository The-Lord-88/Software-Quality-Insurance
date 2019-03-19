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

    def clear(self):
        self.operand1 = "0"
        self.operand2 = ""
        self.operator = ""
        self.last_operand2 = ""
        self.last_operator = ""
        self.model.display = self.operand1

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
        self.operand1 = str(float(self.operand1) + float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def substraction(self):
        self.operand1 = str(float(self.operand1) - float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def multiplication(self):
        self.operand1 = str(float(self.operand1) * float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def division(self):
        if self.operand2 == "0":
            self.operand1 = "Division by 0"
        else:
            self.operand1 = str(float(self.operand1) / float(self.operand2)).rstrip('0').rstrip('.')
        self.operand2 = ""
        self.operator = ""
        self.model.display = self.operand1

    def positive_negative(self):
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


    def add_float(self):
        if self.operand2 == "":
            if "." not in self.operand1:
                self.operand1 += "."
            self.model.display = self.operand1
        else:
            if "." not in self.operand2:
                self.operand2 += "."
            self.model.display = self.operand2

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

    def button_pressed(self, button_label):
        if self.operand1 == "Division by 0":
            self.operand1 = "0"
            self.operand2 = ""
            self.operator = ""

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

        if button_label == "CE":
            self.clear_entry()
        if button_label == "C":
            self.clear()
        if button_label == "Del":
            self.delete()

        if button_label == "+/-":
            self.positive_negative()
        if button_label == ".":
            self.add_float()

        if button_label == "=":
            self.calculate()
        else:
            if self.operand2 == "" and self.operator == "":
                self.model.display = self.operand1
            elif self.operand2 == "" and self.operator != "":
                self.model.display = self.operator
            elif self.operand2 != "" and self.operator != "":
                self.model.display = self.operand2
