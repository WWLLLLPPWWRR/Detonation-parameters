import detonation_calculation

from tkinter import *
from tkinter.ttk import Combobox


def result_window(density, m, m1, m2, m3, material_list, material_list1, material_list2, material_list3):
    den = float(density.get())
    percentage = [float(m.get()), float(m1.get()), float(m2.get()), float(m3.get())]
    material_names = [Combobox.get(material_list), Combobox.get(material_list1), Combobox.get(material_list2), Combobox.get(material_list3)]
    print(material_names, percentage, den)

    # Test for 100%
    if sum(percentage) == 100:
        window_result = Tk()
        window_result.title('Расчёт термохимических характеристик взрывчатых веществ')
        window_result.geometry('450x350')

        result = detonation_calculation.detonation(material_names, percentage, den)
        for i in range(len(result)):
            kbzz = Label(window_result, text=result[i])
            kbzz.grid(column=1, row=i + 1, padx=4, pady=2)

    else:
        window_error = Tk()
        window_error.title('Расчёт термохимических характеристик взрывчатых веществ')
        window_error.geometry('200x100')
        b1 = Label(window_error, text="Quantity's more or less 100%")
        b1.grid(column=1, row=1)


def start_window():
    window = Tk()
    window.title('Расчёт термохимических характеристик взрывчатых веществ')
    window.geometry('600x250')

    b1 = Label(window, text="Взрывчатое вещество")
    b1.grid(column=1, row=1)

    b2 = Label(window, text="Массовая доля ВВ, %")
    b2.grid(column=2, row=1, padx=3, pady=5)

    b3 = Label(window, text="Плотность смесевого ВВ, г/см3")
    b3.grid(column=3, row=1)

    q1 = StringVar(window, value='0.9')

    density = Entry(window, width=10, textvariable=q1)
    density.grid(column=3, row=2, padx=10, pady=5)

    q2 = StringVar(window, value='25')

    m = Entry(window, width=10, textvariable=q2)
    m.grid(column=2, row=2)

    material_list = Combobox(window, width=30)
    material_list.grid(column=1, row=2)
    material_list['values'] = (
    'Аммиачная селитра (NH4NO3)', 'Минеральное масло (C12H26)', 'Тротил (C7H5N3O6)', 'Нитроглицирин (C3H5O9N3)',
    'Алюминий (Al)', 'Дизельное топливо (C13H20)', 'Нитрогликоль (C2H4O6N2)', 'Гексоген (C3H6N6O6)', 'ТНТ (C5H8N4O12)',
    'Октоген (C4H8N8O8)')
    material_list.current(0)

    q3 = StringVar(window, value='25')

    m1 = Entry(window, width=10, textvariable=q3)
    m1.grid(column=2, row=3, padx=5, pady=5)

    material_list1 = Combobox(window, width=30)
    material_list1.grid(column=1, row=3, padx=20, pady=5)
    material_list1['values'] = (
    'Аммиачная селитра (NH4NO3)', 'Минеральное масло (C12H26)', 'Тротил (C7H5N3O6)', 'Нитроглицирин (C3H5O9N3)',
    'Алюминий (Al)', 'Дизельное топливо (C13H20)', 'Нитрогликоль (C2H4O6N2)', 'Гексоген (C3H6N6O6)', 'ТНТ (C5H8N4O12)',
    'Октоген (C4H8N8O8)')
    material_list1.current(1)

    q4 = StringVar(window, value='25')

    m2 = Entry(window, width=10, textvariable=q4)
    m2.grid(column=2, row=4)

    material_list2 = Combobox(window, width=30)
    material_list2.grid(column=1, row=4, padx=5, pady=5)
    material_list2['values'] = (
    'Аммиачная селитра (NH4NO3)', 'Минеральное масло (C12H26)', 'Тротил (C7H5N3O6)', 'Нитроглицирин (C3H5O9N3)',
    'Алюминий (Al)', 'Дизельное топливо (C13H20)', 'Нитрогликоль (C2H4O6N2)', 'Гексоген (C3H6N6O6)', 'ТНТ (C5H8N4O12)',
    'Октоген (C4H8N8O8)')
    material_list2.current(2)

    q5 = StringVar(window, value='25')

    m3 = Entry(window, width=10, textvariable=q5)
    m3.grid(column=2, row=5)

    material_list3 = Combobox(window, width=30)
    material_list3.grid(column=1, row=5, padx=5, pady=5)
    material_list3['values'] = (
    'Аммиачная селитра (NH4NO3)', 'Минеральное масло (C12H26)', 'Тротил (C7H5N3O6)', 'Нитроглицирин (C3H5O9N3)',
    'Алюминий (Al)', 'Дизельное топливо (C13H20)', 'Нитрогликоль (C2H4O6N2)', 'Гексоген (C3H6N6O6)', 'ТНТ (C5H8N4O12)',
    'Октоген (C4H8N8O8)')
    material_list3.current(3)

    def fn():
        result_window(density, m, m1, m2, m3, material_list, material_list1, material_list2, material_list3)
    calc_button = Button(window, text="Рассчитать", width=15, command=fn)
    calc_button.grid(column=3, row=6, padx=5, pady=50)

    window.mainloop()


if __name__ == '__main__':
    start_window()

__version__ = '2.0'
