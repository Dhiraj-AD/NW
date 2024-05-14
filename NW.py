import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.equation = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.equation, width=25, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_list = [
            'C', '', '', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]
        row = 1
        col = 0
        for text in button_list:
            button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, value):
        if value == '=':
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except:
                self.equation.set("Error")
        elif value == 'C':
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + str(value))

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
