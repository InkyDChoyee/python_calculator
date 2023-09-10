from tkinter import*


#label = Label(tk,text='Hello World!')
#label.pack()
#tk.mainloop()

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2 

def divid(num1, num2):
    if num2 == 0:
        print("0으로 나눌 수 없습니다")
        return
    else:
        return num1 / num2
    

tk = Tk()
button11 = Button(tk, text = '더하기', command = '+')
button12 = Button(tk, text = '빼기', command = '-')
button13 = Button(tk, text = '곱하기', command = '*')
button14 = Button(tk, text = '나누기', command= '/')

button11.pack(side = LEFT, padx = 10, pady = 10)
button12.pack(side = LEFT, padx = 10, pady = 10)
button13.pack(side = LEFT, padx = 10, pady = 10)
button14.pack(side = LEFT, padx = 10, pady = 10)

tk.mainloop()