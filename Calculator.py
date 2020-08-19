import tkinter as tk
from tkinter import END, ttk
from tkinter.filedialog import asksaveasfile
# Root
root = tk.Tk()
root.title('Calculator')
root.configure(bg='#202429')
root.attributes('-alpha', 0.95)
root.resizable(width=False, height=False)
root.iconbitmap('C:/Users/HOK THAI/Pictures/Camera Roll/favicon.ico')
operator = ()
# Functions


def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    asksaveasfile(filetypes=files, defaultextension=files)


btn = ttk.Button(root, text='Save', command=lambda: save())
btn.grid(column=4, row=0)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_pi():
    entry.delete(0, END)
    entry.insert(0, '3.1415926535897932384626433832795')


def button_e():
    entry.delete(0, END)
    entry.insert(0, '2.7182818284590452353602874713527')


def button_add():
    entry.get()
    first_number = entry.get()
    global first_num
    global op
    first_num = float(first_number)
    entry.delete(0, END)
    op = '+'


def button_subtract():
    entry.get()
    first_number = entry.get()
    global first_num
    global op
    first_num = float(first_number)
    entry.delete(0, END)
    op = '-'


def button_multiply():
    entry.get()
    first_number = entry.get()
    global first_num
    global op
    first_num = float(first_number)
    entry.delete(0, END)
    op = '*'


def button_divide():
    entry.get()
    first_number = entry.get()
    global first_num
    global op
    first_num = float(first_number)
    entry.delete(0, END)
    op = '/'


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    if op == '+':
        entry.insert(0, first_num + (float(second_number)))

    elif op == '*':
        entry.insert(0, first_num * (float(second_number)))

    elif op == '-':
        entry.insert(0, first_num - (float(second_number)))

    elif op == '/':
        entry.insert(0, first_num / (float(second_number)))


def button_clear():
    entry.delete(0, END)


def button_delete():
    length = len(entry.get())
    entry.delete(length-1, END)


def button_dot():
    length = len(entry.get())
    entry.insert(length, '.')





entry = tk.Entry(root, width=35, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

# Number Buttons
button1 = tk.Button(root, text='1', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(1))
button2 = tk.Button(root, text='2', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(2))
button3 = tk.Button(root, text='3', padx=45, pady=20, bg='black', fg='white', command=lambda: button_click(3))
button4 = tk.Button(root, text='4', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(4))
button5 = tk.Button(root, text='5', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(5))
button6 = tk.Button(root, text='6', padx=45, pady=20, bg='black', fg='white', command=lambda: button_click(6))
button7 = tk.Button(root, text='7', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(7))
button8 = tk.Button(root, text='8', padx=40, pady=20, bg='black',  fg='white', command=lambda: button_click(8))
button9 = tk.Button(root, text='9', padx=45, pady=20, bg='black', fg='white', command=lambda: button_click(9))
button0 = tk.Button(root, text='0', padx=40, pady=20, bg='black', fg='white', command=lambda: button_click(0))

# Op Buttons
button_plus = tk.Button(root, text='+', padx=40, pady=20, bg='#17181A', fg='white', command=button_add)
button_subtract = tk.Button(root, text='-', padx=40, pady=20, bg='#17181A', fg='white', command=button_subtract)
button_multiply = tk.Button(root, text='*', padx=40, pady=20, bg='#17181A', fg='white', command=button_multiply)
button_divide = tk.Button(root, text='/', padx=40, pady=20, bg='#17181A', fg='white', command=button_divide)
button_dot = tk.Button(root, text='.', padx=45, pady=20, bg='#17181A', fg='white', command=button_dot)

# Other Buttons
button_clear = tk.Button(root, text='Clr', padx=36, pady=20, bg='#17181A', fg='white', command=button_clear)
button_delete = tk.Button(root, text='Del', padx=34, pady=20, bg='#17181A', fg='white', command=button_delete)
button_equal = tk.Button(root, text='=', padx=40, pady=20, bg='#17181A', fg='white', command=button_equal)
button_pi = tk.Button(root, text='π', padx=45, pady=20, bg='#17181A', fg='white', command=button_pi)
button_e = tk.Button(root, text='e', padx=40, pady=20, bg='#17181A', fg='white', command=button_e)

# Place Number Buttons
button1.grid(row=4, column=2)
button2.grid(row=4, column=1)
button3.grid(row=4, column=0)
button4.grid(row=3, column=2)
button5.grid(row=3, column=1)
button6.grid(row=3, column=0)
button7.grid(row=2, column=2)
button8.grid(row=2, column=1)
button9.grid(row=2, column=0)
button0.grid(row=5, column=1)

# Place Operator Buttons
button_multiply.grid(row=2, column=4)
button_plus.grid(row=4, column=4)
button_subtract.grid(row=3, column=4)
button_divide.grid(row=1, column=4)
button_dot.grid(row=5, column=0)

# Place Other Buttons
button_clear.grid(row=1, column=2)
button_delete.grid(row=5, column=2)
button_equal.grid(row=5, column=4)
button_pi.grid(row=1, column=0)
button_e.grid(row=1, column=1)

root.mainloop()
