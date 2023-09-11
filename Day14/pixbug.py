import tkinter as tk

error_flag = False 

def select(value):
    global error_flag
    if not error_flag:
        start = result_label.cget("text")
        if start == "0":
            result_label.config(text=value)
        else:
            result_label.config(text= start + value)

def reset():
    global error_flag
    result_label.config(text="0")
    error_flag = False

def calculate():
    global error_flag
    try:
        result = eval(result_label.cget("text"))
        result_label.config(text=str(result))
    except Exception as e:
        result_label.config(text="0으로는 나눌 수 없습니다\n"+"C 버튼을 눌러 리셋해주세요")
        error_flag = True


root = tk.Tk()
root.title("계산기")
  
row_count = 5
col_count = 4

result_label = tk.Label(root, text="0", font=("Helvetica", 24))
result_label.grid(row=0, column=0, columnspan=col_count, padx=25, pady=25)

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "C", "0", "=", "/"
]

row = 1
col = 0

for button_text in buttons:
    if button_text == "=":
        button = tk.Button(root, text=button_text, command = calculate)
    elif button_text == "C":
        button = tk.Button(root, text=button_text, command = reset)
    else:
        button = tk.Button(root, text=button_text, command=lambda v=button_text: select(v))
    
    button.grid(row=row, column=col, padx=25, pady=25)
    col += 1
    if col >= col_count:
        col = 0
        row += 1

root.mainloop()