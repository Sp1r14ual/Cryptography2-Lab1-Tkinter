from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from pollards import pollards_p_minus_1


def click_button():
    n_filename = n_entry.get()
    n_file = None
    n = None

    p_filename = p_entry.get()
    p_file = None
    p = None

    try:
        if not (".txt" in n_filename):
            raise FileExistsError("Некорректное имя файла со значением n")

        if not (".txt" in p_filename):
            raise FileExistsError("Некорректное имя файла со значением p")

        try:
            n_file = open(n_filename, "r")
            p_file = open(p_filename, "r")
        except:
            raise FileNotFoundError("Не удалось открыть файл(ы)")

        try:
            n = int(n_file.read())
            p = int(p_file.read())
        except:
            raise ValueError("Некорректные входные данные")

    except Exception as E:
        showerror("Ошибка", str(E))
        return

    result = pollards_p_minus_1(n, p)

    with open("output.txt", mode="w") as output_file:
        output_file.write(str(result))

    showinfo("Выполнено", "Результат работы программы записан в файл output.txt")

    return


root = Tk()
root.title("Pollard's p − 1 algorithm")
root.geometry("400x400+200+150")

root.resizable(False, False)

n_label = ttk.Label(text="Файл со значением n", font=("Arial", 14))
n_label.pack(pady=10)

n_entry = ttk.Entry(justify=CENTER)
n_entry.pack()

p_label = ttk.Label(text="Файл со значением p", font=("Arial", 14))
p_label.pack(pady=10)

p_entry = ttk.Entry(justify=CENTER)
p_entry.pack()

btn = ttk.Button(text="Пуск", command=click_button)
btn.pack(pady=10)

root.mainloop()
