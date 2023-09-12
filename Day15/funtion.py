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