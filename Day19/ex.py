import tkinter as tk
import re

class Calculator:
    def __init__(self):
        self.last_input_operator = False
        self.result_displayed = False 

    def reset(self):
        self.enable_number_buttons()
        result_label.config(text="0")
        self.last_input_operator = False
        self.result_displayed = False

    def calculate(self):
        try:
            expression = result_label.cget("text")
        
            expression = re.sub(r'(?<=[+\-*/])0+(?=\d)', '', expression)
            
            if expression == "0" or expression == "0으로 못 나눔!":
                self.result_displayed = True
                self.reset()
                self.enable_number_buttons()
                return

            result = eval(expression)
            result_str = "{:.7f}".format(result)
            result_str = result_str.rstrip("0").rstrip(".") if "." in result_str else result_str
            result_label.config(text=result_str)
            self.result_displayed = True
            self.disable_number_buttons()
        except ZeroDivisionError:
            result_label.config(text="0으로 못 나눔!")
            self.last_input_operator = False
            self.enable_number_buttons()
            self.result_displayed = True
            self.enable_number_buttons()

    def select(self, value):
        current_text = result_label.cget("text")
        
        if self.result_displayed:
            if value.isdigit() or value == ".":
                self.result_displayed = False
            elif value in ("+", "-", "*", "/"):
                self.enable_number_buttons()
                self.result_displayed = False
                self.last_input_operator = True
                if current_text and current_text[-1] in ("+", "-", "*", "/"):
                    result_label.config(text=current_text[:-1] + value)
                else:
                    result_label.config(text=current_text + value)
        else:
            if len(current_text.replace(".", "")) >= 12:
                return
            
            if self.last_input_operator and value in ("+", "-", "*", "/"):
                result_label.config(text=current_text[:-1] + value)
                return

            if current_text == "0" or current_text == "0.":
                if value == "0" or value.isdigit():
                    result_label.config(text=value)
                else:
                    result_label.config(text=current_text + value)
            elif current_text == "0으로 못 나눔!":
                result_label.config(text=value)
            else:
                result_label.config(text=current_text + value)

            if value in ("+", "-", "*", "/"):
                self.last_input_operator = True
            else:
                self.last_input_operator = False

    def disable_number_buttons(self):
        for button in number_buttons:
            button.config(state="disabled")

    def enable_number_buttons(self):
        for button in number_buttons:
            button.config(state="normal")

calculator = Calculator()

root = tk.Tk()
root.title("계산기")
root.resizable(False, False)

row_count = 5
col_count = 4

result_label = tk.Label(root, text="0", relief="sunken", borderwidth=5, font=("맑은 고딕", 40), bg="black", fg="white", anchor="e")
result_label.grid(row=0, column=0, columnspan=col_count, padx=15, pady=15, rowspan=1, sticky="we")

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "C", "0", "=", "/"
]
button_width = 6
button_height = 2
button_font = "맑은 고딕", 20, "bold"

row = 1
col = 0

number_buttons = []

for button_text in buttons:
    if button_text == "=":
        button = tk.Button(root, text=button_text, command=calculator.calculate, bg="gray", fg="white", width=button_width, height=button_height, font=button_font)
    elif button_text == "C":
        button = tk.Button(root, text=button_text, command=calculator.reset, bg="white", fg="black", width=button_width, height=button_height, font=button_font)
    elif button_text in ("+", "-", "*", "/"):
        button = tk.Button(root, text=button_text, command=lambda v=button_text: calculator.select(v), bg="#fafa96", fg="black", width=button_width, height=button_height, font=button_font)
    else:
        button = tk.Button(root, text=button_text, command=lambda v=button_text: calculator.select(v), bg="#cfffe5", fg="black", width=button_width, height=button_height, font=button_font)
        number_buttons.append(button)

    button.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col >= col_count:
        col = 0
        row += 1

root.mainloop()
