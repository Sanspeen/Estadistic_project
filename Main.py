import os
import time
import sys
from menu_point_1 import *
from Data import database

os.system('cls')
print("██████╗░██████╗░░█████╗░██╗░░░██╗███████╗░█████╗░████████╗░█████╗░  ██████╗░███████╗\n" +
      "██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝\n" +
      "██████╔╝██████╔╝██║░░██║░╚████╔╝░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║  ██║░░██║█████╗░░\n" +
      "██╔═══╝░██╔══██╗██║░░██║░░╚██╔╝░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║  ██║░░██║██╔══╝░░\n" +
      "██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝  ██████╔╝███████╗\n" +
      "╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░  ╚═════╝░╚══════╝\n" +

      "███████╗░██████╗████████╗░█████╗░██████╗░██╗░██████╗████████╗██╗░█████╗░░█████╗░░░░░░░░░░\n" +
      "██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██║██╔══██╗██╔══██╗░░░░░░░░░\n" +
      "█████╗░░╚█████╗░░░░██║░░░███████║██║░░██║██║╚█████╗░░░░██║░░░██║██║░░╚═╝███████║░░░░░░░░░\n" +
      "██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░██║██║░╚═══██╗░░░██║░░░██║██║░░██╗██╔══██║░░░░░░░░░\n" +
      "███████╗██████╔╝░░░██║░░░██║░░██║██████╔╝██║██████╔╝░░░██║░░░██║╚█████╔╝██║░░██║██╗██╗██╗\n" +
      "╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝╚═╝\n")
time.sleep(3)
os.system('cls')
print(
    '██████╗░░█████╗░██████╗░  ░██████╗░█████╗░███╗░░██╗████████╗██╗░█████╗░░██████╗░░█████╗░\n' +
    '██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔══██╗████╗░██║╚══██╔══╝██║██╔══██╗██╔════╝░██╔══██╗\n' +
    '██████╔╝██║░░██║██████╔╝  ╚█████╗░███████║██╔██╗██║░░░██║░░░██║███████║██║░░██╗░██║░░██║\n' +
    '██╔═══╝░██║░░██║██╔══██╗  ░╚═══██╗██╔══██║██║╚████║░░░██║░░░██║██╔══██║██║░░╚██╗██║░░██║\n' +
    '██║░░░░░╚█████╔╝██║░░██║  ██████╔╝██║░░██║██║░╚███║░░░██║░░░██║██║░░██║╚██████╔╝╚█████╔╝\n' +
    '╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░\n' +

    '███████╗██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ███╗░░░███╗███████╗░░░░░██╗██╗░█████╗░\n' +
    '██╔════╝██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ████╗░████║██╔════╝░░░░░██║██║██╔══██╗\n' +
    '█████╗░░██████╔╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██╔████╔██║█████╗░░░░░░░██║██║███████║\n' +
    '██╔══╝░░██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║╚██╔╝██║██╔══╝░░██╗░░██║██║██╔══██║\n' +
    '██║░░░░░██║░░██║██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ██║░╚═╝░██║███████╗╚█████╔╝██║██║░░██║\n' +
    '╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝░╚════╝░╚═╝╚═╝░░╚═╝\n')
time.sleep(3)
os.system('cls')

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
            continue_variables_for_users = ['altura', 'peso', 'volver a casa', 'promedio del semestre']
            continue_variables = ['height', 'weight', 'timeBackingHouse', 'lastSemesterAvg']

            print('Las variables disponibles son:[altura, peso, volver a casa, promedio del semestre]')
            var_1 = input('\nIngrese el nombre de la primer variable aleatoria de la lista para hacer los calculos:')
            var_2 = input('\nIngrese el nombre de la segunda variable aleatoria de la lista para hacer los calculos:')
            try:
                indx_var1 = continue_variables_for_users.index(var_1)
                indx_var2 = continue_variables_for_users.index(var_2)
                point_a(continue_variables[indx_var1], continue_variables[indx_var2])
                input('\nPresione <<ENTER>> para continuar.')

            except:
                print(
                    'Lo siento, pero esa variable o no es continua aleatoria o no existe en nuestra base de datos... Te llevaremos al menú inicial.')
                time.sleep(3)

        if chosen_index == 'b':
            os.system('cls')
            point_b(database)
            input('\nPresione <<ENTER>> para volver al menu principal.')

        if chosen_index == 'c':
            print('Coming soon...')
