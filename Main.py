import time
import os


import menu_point_1
import menu_point_2
import menu_point_3
from Data import *
while True:
    os.system('cls')
    print('Ingrese "salir" cerrar la aplicación.')
    chosen_point = input('Elige el punto el cual deseas ver la solucion (1, 2, 3 ó 4):').lower()
    if chosen_point == 'salir':
        break

    if chosen_point == '1':
        os.system('cls')
        print('Ingrese "x" para regresar al menú anterior.')
        chosen_index = input(
            "Elige el indice de del punto el cual deseas ver la solución (a, b, c, d, e, f, g ó h):").lower()

        if chosen_index == 'x':
            continue

        if chosen_index == 'a':
            os.system('cls')
            #THIS BLOCK WILL BE MIGRATED TO TKINTER APP.

            #Those variable names will have to be selected by buttons.

            print('Las variables disponibles son: (altura, peso, volver a casa, promedio del semestre)')
            var_1 = input('\nIngrese el nombre de la primer variable aleatoria de la lista para hacer los calculos:')
            var_2 = input('\nIngrese el nombre de la segunda variable aleatoria de la lista para hacer los calculos:')
            #You have to delete this try
            try:
                continue_variables_for_users = ['altura', 'peso', 'volver a casa', 'promedio del semestre']
                indx_var1 = continue_variables_for_users.index(var_1)
                indx_var2 = continue_variables_for_users.index(var_2)

                continue_variables = ['height', 'weight', 'timeBackingHouse', 'lastSemesterAvg']
                menu_point_1.point_a(continue_variables[indx_var1], continue_variables[indx_var2], var_1, var_2)
                input('\nPresione <<ENTER>> para continuar.')
            #SINCE HERE.
            except:
                print(
                    'Lo siento, pero esa variable o no es continua aleatoria o no existe en nuestra'
                    ' base de datos... Te llevaremos al menú inicial.')
                time.sleep(3)

        if chosen_index == 'b':
            os.system('cls')
            #THIS BLOCK WILL BE MIGRATED TO TKINTER APP.
            covariance, cov_answer = menu_point_1.point_b(data_base)
            #THIS PART WILL BE DISPLAYED INTO THE APP
            print(f"Covarianza entre Val. Matricula y Estrato: {covariance}\nConclusion 1: {cov_answer}")
            #SINCE HERE.
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'c':
            os.system('cls')
            #THIS BLOCK WILL BE MIGRATED TO TKINTER APP.
            menu_point_1.point_c(data_base)
            #INSIDE THIS METHOD A LOT OF THINGS WILL BE RETURNED.
            #SINCE HERE.
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'd':
            os.system('cls')
            menu_point_1.point_d(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'e':
            os.system('cls')
            menu_point_1.point_e()
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'f':
            os.system('cls')
            menu_point_1.point_f()
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'g':
            os.system('cls')
            menu_point_1.point_g()
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'h':
            os.system('cls')
            menu_point_1.point_h()
            input('\nPresione <<ENTER>> para volver al menu principal.')

    if chosen_point == '2':
        os.system('cls')
        print('Ingrese "x" para regresar al menú anterior.')
        chosen_index = input("Elige el indice de del punto el cual deseas ver la solución (a, b, c, d, e, f ó g):")\
            .lower()

        if chosen_index == 'a':
            os.system('cls')
            menu_point_2.point_a(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'b':
            os.system('cls')
            menu_point_2.point_b(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'c':
            os.system('cls')
            menu_point_2.point_c(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'd':
            os.system('cls')
            menu_point_2.point_d(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'e':
            os.system('cls')
            menu_point_2.point_e(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'f':
            os.system('cls')
            menu_point_2.point_f(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'g':
            os.system('cls')
            menu_point_2.point_g(data_base)
            input('\nPresione <<ENTER>> para volver al menu principal.')

    if chosen_point == '3':
        os.system('cls')
        print('Ingrese "x" para regresar al menú anterior.')
        chosen_index = input("Elige el indice de del punto el cual deseas ver la solución (a, b, c, d):") \
            .lower()

        if chosen_index == 'a':
            os.system('cls')
            menu_point_3.point_a(drinks_data)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'b':
            os.system('cls')
            menu_point_3.point_b(drinks_data)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'c':
            os.system('cls')
            menu_point_3.point_c()
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'd':
            os.system('cls')
            menu_point_3.point_d(drinks_data)
            input('\nPresione <<ENTER>> para volver al menu principal.')

    if chosen_point == '4':
        os.system('cls')
        print('Ingrese "x" para regresar al menú anterior.')
        chosen_index = input("Link del colab:"
                             " https://colab.research.google.com/drive/1ZH2fpBb_5MjKdIbqIpMBttCwNn4uA5HD?usp=sharing") \
            .lower()
