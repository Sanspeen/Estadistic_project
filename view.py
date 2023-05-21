import tkinter as tk
from tkinter import messagebox, ttk
import menu_point_1
import menu_point_2
import menu_point_3
from Functions import *
from Data import *

# Indices de la pagina 1.


# Indice A
continue_variables_for_users = ['altura', 'peso', 'volver a casa', 'promedio del semestre']
answer = ""

def show_results(user_val_1, user_val_2, result_lbl):

    indx_var1 = continue_variables_for_users.index(user_val_1)
    indx_var2 = continue_variables_for_users.index(user_val_2)

    continue_variables = ['height', 'weight', 'timeBackingHouse', 'lastSemesterAvg']
    answer = menu_point_1.point_a(continue_variables[indx_var1], continue_variables[indx_var2], user_val_1, user_val_2)
    result_lbl.config(text=f"Resultados: \n{answer}")

def open_page_1_indx_1():
    new_window = tk.Toplevel(app)
    new_window.title("Punto a")
    new_window.geometry("900x900")
    new_window.configure(bg='#7587c6')

    label = tk.Label(new_window, text=f"Esta es la página", font=("Arial", 14), bg='#7587c6', fg='#ffffff')
    label.pack(pady=30)
    combo_1 = ttk.Combobox(
        new_window,
        state="readonly",
        values=continue_variables_for_users
    )

    combo_1.pack(pady=20)

    combo_2 = ttk.Combobox(
        new_window,
        state="readonly",
        values=continue_variables_for_users
    )

    combo_2.pack(pady=15)

    back_button = tk.Button(new_window, text="Volver", command=new_window.destroy, font=("Arial", 12), bg='#465ca9',
                            fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=0)

    result_lbl = tk.Label(new_window, text=f"Resultados:")
    result_lbl.pack(pady=5)

    submit_btn = tk.Button(new_window, text="Resultados", command=lambda: show_results(combo_1.get(), combo_2.get(), result_lbl),
                           font=("Arial", 12), bg='#465ca9',
                           fg='#ffffff', padx=20, pady=5)

    submit_btn.pack(pady=11)

#Termina punto 1.

def show_frame(frame):
    frame.tkraise()


def create_button_frame(master, text):
    frame = tk.Frame(master, bg='#7587c6')
    label = tk.Label(frame, text=text, font=("Arial", 18), bg='#465ca9', fg='#ffffff')
    label.pack(pady=30)
    back_button = tk.Button(frame, text="Volver", command=lambda: show_frame(main_frame), font=("Arial", 12),
                            bg='#465ca9', fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=10)
    return frame


def open_page(page_name):
    new_window = tk.Toplevel(app)
    new_window.title(page_name)
    new_window.geometry("600x500")
    new_window.configure(bg='#7587c6')

    label = tk.Label(new_window, text=f"Esta es la página {page_name}", font=("Arial", 14), bg='#7587c6', fg='#ffffff')
    label.pack(pady=30)

    back_button = tk.Button(new_window, text="Volver", command=new_window.destroy, font=("Arial", 12), bg='#465ca9',
                            fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=10)


app = tk.Tk()
app.title("Proyecto estadística")
app.geometry("600x500")
app.configure(bg='#7587c6')

main_frame = tk.Frame(app, bg='#5168b7')
main_frame.place(x=0, y=0, width=600, height=500)

title_label = tk.Label(main_frame, text="Proyecto estadística", font=("Arial", 20, "bold"), bg='#6377bf', fg='#ffffff')
title_label.pack(pady=20)

# Ventana 1
window1 = create_button_frame(app, "Esta es la ventana 1")
window1.place(x=0, y=0, width=600, height=500)
button1 = tk.Button(main_frame, text="Ventana 1", command=lambda: show_frame(window1), font=("Arial", 12), bg='#4d4d4d',
                   fg='#ffffff', padx=20, pady=5)
button1.pack(fill=tk.X, padx=50, pady=10)

i = 0
btn_1 = tk.Button(window1, text=f"Punto a", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                  command=lambda p=i: open_page_1_indx_1())
btn_1.pack(pady=5)

# Ventana 2
window2 = create_button_frame(app, "Esta es la ventana 2")
window2.place(x=0, y=0, width=600, height=500)
button2 = tk.Button(main_frame, text="Ventana 2", command=lambda: show_frame(window2), font=("Arial", 12), bg='#4d4d4d',
                   fg='#ffffff', padx=20, pady=5)
button2.pack(fill=tk.X, padx=50, pady=10)

for i in range(1, 8):
    btn_1 = tk.Button(window2, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                      command=lambda p=i: open_page(f"Página {p}"))
    btn_1.pack(pady=5)

# Ventana 3
window3 = create_button_frame(app, "Esta es la ventana 3")
window3.place(x=0, y=0, width=600, height=500)
button3 = tk.Button(main_frame, text="Ventana 3", command=lambda: show_frame(window3), font=("Arial", 12), bg='#4d4d4d',
                   fg='#ffffff', padx=20, pady=5)
button3.pack(fill=tk.X, padx=50, pady=10)

for i in range(1, 8):
    btn_1 = tk.Button(window3, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                      command=lambda p=i: open_page(f"Página {p}"))
    btn_1.pack(pady=5)

# Ventana 4
window4 = create_button_frame(app, "Esta es la ventana 4")
window4.place(x=0, y=0, width=600, height=500)
button4 = tk.Button(main_frame, text="Ventana 4", command=lambda: show_frame(window4), font=("Arial", 12), bg='#4d4d4d',
                   fg='#ffffff', padx=20, pady=5)
button4.pack(fill=tk.X, padx=50, pady=10)

for i in range(1, 8):
    btn_1 = tk.Button(window4, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                      command=lambda p=i: open_page(f"Página {p}"))
    btn_1.pack(pady=5)

show_frame(main_frame)
app.mainloop()
