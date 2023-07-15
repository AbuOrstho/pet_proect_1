import tkinter as tk

window = tk.Tk()  # Создает окно
window.geometry('400x300')  # Задает размер окна
window.title("Калькулятор")  # Титульное название окна
window.resizable(0, 0)  # Запрет на изменение размера
window.configure(bg='#202020')  # Устанавливаем цвет фона

p1 = tk.Frame(pady=4, bg='#202020', height=10)  # Создание фреймов
p2 = tk.Frame(pady=10, bg='#202020', height=10)
p3 = tk.Frame(bg='blue')

pol = tk.Entry(master=p1, font=('Times New Roman', 15, 'bold'), bg='#4E5754', fg='#ffffff',
               width=36)  # Создание виджетов с полем для ввода и ответа
otv = tk.Entry(master=p3, font=('Times New Roman', 15, 'bold'), bg='#4E5754', fg='#ffffff', width=36)
pol.pack(side=tk.LEFT, expand=True)
otv.pack(side=tk.RIGHT, expand=True)
p1.pack()
p3.pack()


def calc():  # Функция для решения примера и вывода ответа
    try:
        x = pol.get()
        result = eval(x)
        otv.delete(0, tk.END)
        otv.insert(tk.END, result)
    except ZeroDivisionError:
        otv.delete(0, tk.END)
        pol.delete(0, tk.END)
        otv.insert(0, 'На ноль делить нельзя')
    except:
        otv.delete(0, tk.END)
        pol.delete(0, tk.END)
        otv.insert(0, 'Ошибка')


def add_to_entry(value):  # Функция для добавления символа при нажатии на кнопку
    current_text = pol.get()
    pol.delete(0, tk.END)
    pol.insert(tk.END, current_text + value)


def delete():  # Функция для удаления последнего элемента из строки
    current_text = pol.get()
    update_text = current_text[0:-1]
    pol.delete(0, tk.END)
    pol.insert(tk.END, update_text)


def all_delete():  # Функция для удаления всей строки
    pol.delete(0, tk.END)


buttons = (('(', ')', '<', 'C'),
           ('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '+', '='))  # Текст для кнопок

for row in range(5):  # Цикл для создания и добавления кнопок
    for col in range(4):
        button_text = buttons[row][col]
        if button_text == '=':
            tk.Button(master=p2, width=7, bg='#76b9ed', fg='#213442', font=('Times New Roman', 15), text=button_text,
                      command=calc).grid(
                row=row + 2, column=col, padx=3,
                pady=3)
        elif button_text == '<':
            tk.Button(master=p2, width=7, bg='#3b3b3b', fg='#ffffff', font=('Times New Roman', 15), text=button_text,
                      command=delete).grid(
                row=row + 2, column=col, padx=3,
                pady=3)
        elif button_text == 'C':
            tk.Button(master=p2, width=7, bg='#3b3b3b', fg='#ffffff', font=('Times New Roman', 15), text=button_text,
                      command=all_delete).grid(
                row=row + 2, column=col, padx=3,
                pady=3)
        else:
            tk.Button(master=p2, width=7, bg='#3b3b3b', fg='#ffffff', font=('Times New Roman', 15), text=button_text,
                      command=lambda val=button_text: add_to_entry(val)).grid(row=row + 2, column=col, padx=3, pady=3)
p2.pack()
window.mainloop()
