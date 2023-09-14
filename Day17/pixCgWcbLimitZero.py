import tkinter

class Calculator:
    def __init__(self):
        self.current_value = 0
        self.result = None
        self.operator = None

    def reset(self):
        self.current_value = 0
        self.result = None
        self.operator = None

    def calculate(self, operator, operand):
        if operator == '+':
            self.current_value += operand
        elif operator == '-':
            self.current_value -= operand
        elif operator == '*':
            self.current_value *= operand
        elif operator == '/':
            if operand != 0:
                self.current_value /= operand
            else:
                print("Error: Division by zero")
                return False
        return True

    def handle_input(self, input_str):
        if input_str.isdigit():
            if self.result is not None:
                print("Error: Cannot input numbers after getting a result")
            else:
                self.current_value = int(input_str)
        elif input_str in ['+', '-', '*', '/']:
            if self.result is not None or self.current_value == 0:
                print("Error: Cannot input operators in this state")
            else:
                self.operator = input_str
        elif input_str == '=':
            if self.result is None and self.operator is not None:
                print("Error: Incomplete expression")
            elif self.operator is not None:
                operand = self.current_value
                if self.calculate(self.operator, operand):
                    self.result = self.current_value
                    print(f"Result: {self.result}")
        elif input_str == 'C':
            self.reset()
        else:
            print("Error: Invalid input")

if __name__ == "__main__":
    calc = Calculator()
    while True:
        input_str = input("Enter a number, operator (+, -, *, /), =, or C (to reset): ")
        if input_str.lower() == 'q':
            break
        calc.handle_input(input_str)