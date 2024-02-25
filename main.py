from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from trial_division import trial_division
from sieve import sieve
from pollards import factorize


def click_button():
    n_filename = n_entry.get()
    n_file = None
    n = None

    try:
        if not (".txt" in n_filename):
            raise FileExistsError("Некорректное имя файла со значением n")

        try:
            n_file = open(n_filename, "r")
        except:
            raise FileNotFoundError("Не удалось открыть файл")

        try:
            n = int(n_file.read())
        except:
            raise ValueError("Некорректные входные данные")

    except Exception as E:
        showerror("Ошибка", str(E))
        return

    mode = AlgoOption.get()

    is_prime = None

    if mode == "TrialDivision":
        is_prime = trial_division(n)
    else:
        is_prime = sieve(n)

    if is_prime:
        showwarning("Внимание", "Введенное число является простым")
        return

    calculated, time, iter_count = factorize(n)

    with open("output.txt", mode="w") as output_file:
        output_file.write(" ".join(map(str, calculated)))

    time_entry.delete(0, END)
    iter_count_entry.delete(0, END)

    time_entry.insert(0, time)
    iter_count_entry.insert(0, iter_count)

    showinfo("Выполнено", "Результат работы программы записан в файл output.txt")

    return


root = Tk()
root.title("Pollard's p − 1 algorithm")
root.geometry("400x500+200+150")

root.resizable(False, False)

n_label = ttk.Label(text="Файл со значением n", font=("Arial", 14))
n_label.pack(pady=10)

n_entry = ttk.Entry(justify=CENTER)
n_entry.pack()

primary_check_label = ttk.Label(
    text="Алгоритм проверки на простоту", font=("Arial", 14))
primary_check_label.pack(pady=10)

AlgoOption = StringVar(value="TrialDivision")

TrialDivisionOption = ttk.Radiobutton(
    text="Метод пробных делений", value="TrialDivision", variable=AlgoOption)
TrialDivisionOption.pack(ipady=5)

SieveOption = ttk.Radiobutton(
    text="Решето Эратосфена", value="Sieve", variable=AlgoOption)
SieveOption.pack()

btn = ttk.Button(text="Пуск", command=click_button)
btn.pack(pady=10)

time_label = ttk.Label(text="Время работы алгоритма", font=("Arial", 14))
time_label.pack(pady=10)

time_entry = ttk.Entry(justify=CENTER)
time_entry.pack()

iter_count_label = ttk.Label(
    text="Количество итераций основного цикла", font=("Arial", 14))
iter_count_label.pack(pady=10)

iter_count_entry = ttk.Entry(justify=CENTER)
iter_count_entry.pack()

root.mainloop()
