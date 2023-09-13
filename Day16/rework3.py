import tkinter as tk

class Funtion:
    def select(self, value):
        start = result_label.cget("text")
        if start == "0":
            result_label.config(text=value)
        elif start == "0으로는 나눌 수 없습니다":
            result_label.config(text=value)
        else:
            result_label.config(text= start + value)

    def reset(self):
        result_label.config(text="0")

    def calculate(self):
        try:
            result = eval(result_label.cget("text"))
            result_label.config(text=str(result))
        except ZeroDivisionError:
            result_label.config(text="0으로는 나눌 수 없습니다")

f = Funtion()

root = tk.Tk()
root.title("계산기")

row_count = 5
col_count = 4

outer_label = tk.Label(root, text=" ", relief="sunken", borderwidth=5, font=("Arial", 50), bg="gray", fg="black")
outer_label.grid(row=0, column=0,columnspan=col_count, padx=17, pady=17, rowspan=1, sticky='we')

result_label = tk.Label(outer_label, text="0", relief="sunken", borderwidth=5, font=("맑은 고딕", 40),bg="black", fg="white")
result_label.grid(row=0, column=0, columnspan=col_count, padx=15, pady=15, rowspan=1, sticky="e")




buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "C", "0", "=", "/"
]
button_width = 4
button_height = 2
button_font = 20

row = 1
col = 0

for button_text in buttons:
    if button_text == "=":
        button = tk.Button(root, text=button_text, command=f.calculate, bg="gray", fg="white", width=button_width, height=button_height,font=button_font)
    elif button_text == "C":
        button = tk.Button(root, text=button_text, command=f.reset, bg="white", fg="black", width=button_width, height=button_height, font=button_font)
    elif button_text in ("+", "-", "*", "/"):
        button = tk.Button(root, text=button_text, command=lambda v=button_text: f.select(v) if result_label.cget("text") not in ("0", "0으로는 나눌 수 없습니다") else None, bg="#fafa96", fg="black", width=button_width, height=button_height,font=button_font)
    else:
        button = tk.Button(root, text=button_text, command=lambda v=button_text: f.select(v), bg="#cfffe5", fg="black", width=button_width, height=button_height,font=button_font)
    
    button.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col >= col_count:
        col = 0
        row += 1

root.mainloop()