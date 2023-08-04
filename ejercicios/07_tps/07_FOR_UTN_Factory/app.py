'''
Nombre: Santiago
Apellido: Decibe
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cantidad_postulantes_25 = 0
        contador_post_py  = 0
        contador_post_js  = 0
        contador_post_net = 0

        contador_m  = 0
        contador_f  = 0
        contador_nb = 0

        acumulador_edad_nb = 0
        acumulador_edad_m  = 0
        acumulador_edad_f  = 0

        flag_min = True

        for i in range(1,3,1):

            nombre = prompt('TP 07 - For','Ingrese su nombre: ')
            while nombre == None or nombre.isdigit() or nombre == '' or len(nombre) < 3:
                nombre = prompt('TP 07 - For','Ingrese su nombre: ')

            edad = prompt('TP 07 - For','Ingrese su edad: ')
            while edad == None or edad.isdigit() == False or  int(edad) < 18 or int(edad) > 110:
                edad = prompt('TP 07 - For','Ingrese su edad: ')
            edad = int(edad)

            genero = prompt('TP 07 - For','Ingrese su género: (F - M - NB) ')
            while genero == None or (genero.upper() != 'F' and genero.upper() != 'M' and genero.upper() != 'NB'):
                genero = prompt('TP 07 - For','Ingrese su género: ( F - M - NB ) ')

            tecnologia = prompt('TP 07 - For','Ingrese la tecnología que se utilizará: (PYTHON - JS - ASP.NET) ')
            while tecnologia == None or (tecnologia.upper() != 'PYTHON' and tecnologia.upper() != 'JS' and tecnologia.upper() != 'ASP.NET'):
                tecnologia = prompt('TP 07 - For','Ingrese la tecnología que se utilizará: (PYTHON - JS - ASP.NET) ')

            puesto = prompt('TP 07 - For','Ingrese su puesto: (Jr - Ssr - Sr) ')
            while puesto == None or (puesto.capitalize() != 'Jr' and puesto.capitalize() != 'Ssr' and puesto.capitalize() != 'Sr'):
                puesto = prompt('TP 07 - For','Ingrese su puesto: (Jr - Ssr - Sr) ')


        #A) ===========================================================================
            match genero.upper():
                case 'NB':
                    contador_nb += 1  #E)
                    acumulador_edad_nb += edad #C)
                    match tecnologia.upper():
                        case 'ASP.NET' | 'JS':
                            match puesto.capitalize():
                                case 'Ssr':
                                    if edad > 24 and edad < 41:
                                        cantidad_postulantes_25 += 1 
                case 'M':
                    contador_m += 1  #E)
                    acumulador_edad_m += edad #C)
                case 'F': 
                    contador_f += 1  #E)
                    acumulador_edad_f += edad #C)
        #A) ===========================================================================


        #B) ===========================================================================
            match puesto.capitalize():
                case 'Jr':
                    if flag_min == True:
                        jr_min_edad   = edad
                        jr_min_nombre = nombre
                        flag_min = False
                    else:
                        if edad < jr_min_edad:
                            jr_min_edad   = edad
                            jr_min_nombre = nombre
        #B) ===========================================================================


        #D) ============================================================================
            match tecnologia.upper():
                case 'PYTHON':
                    contador_post_py  += 1
                case 'JS':
                    contador_post_js  += 1
                case 'ASP.NET':
                    contador_post_net += 1

            if contador_post_py > contador_post_js and contador_post_py > contador_post_net:
                # tecn_cantidad_postul_py = contador_post_py
                tecn_nombre_mas_postulantes = 'PYTHON'
            elif contador_post_js > contador_post_net:
                # tecn_cantidad_postul_js = contador_post_js
                tecn_nombre_mas_postulantes = 'JS'
            else:
                # tecn_cantidad_postul_net = contador_post_net
                tecn_nombre_mas_postulantes = 'ASP.NET'
        #D) ===========================================================================

        #! Termina el For

        #C) =========================================================================== 
        if acumulador_edad_m  != 0:
            promedio_m  = acumulador_edad_m  / 10
            alert('TP 07 - For', f'El promedio de edad de los hombres es: {promedio_m}')
        if acumulador_edad_f  != 0:    
            promedio_f  = acumulador_edad_f  / 10
            alert('TP 07 - For', f'El promedio de edad de las mujeres es: {promedio_f}')
        if acumulador_edad_nb != 0:
            promedio_nb = acumulador_edad_nb / 10
            alert('TP 07 - For', f'El promedio de edad del género no binario es: {promedio_nb}')
        #C) ===========================================================================



        #E) ===========================================================================
        if contador_m  != 0:
            porcentaje_m  = contador_m  / 10
            alert('TP 07 - For', f'El porcentaje de postulantes masculinos es: {porcentaje_m}')
        if contador_f  != 0:
            porcentaje_f  = contador_f  / 10
            alert('TP 07 - For', f'El porcentaje de postulantes femeninos es: {porcentaje_f}')
        if contador_nb != 0:
            porcentaje_nb = contador_nb / 10
            alert('TP 07 - For', f'El porcentaje de postulantes no binarios es: {porcentaje_nb}')
        #E) ===========================================================================




#!A)
# Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
# cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
        alert('TP 07 - For', f'La cantidad de postulantes de género No Binario, que aspiran a un puesto Ssr y programan en ASP.NET o JS son: {cantidad_postulantes_25}.')
#!B)
# Nombre del postulante Jr con menor edad.
        alert('TP 07 - For', f'El nombre del postulante Jr más joven es {jr_min_nombre}, con {jr_min_edad} años.')
#!C)
# Promedio de edades por género.
        # alert('TP 07 - For', f'El promedio de edad de los hombres es: {promedio_m}')
        # alert('TP 07 - For', f'El promedio de edad de las mujeres es: {promedio_f}')
        # alert('TP 07 - For', f'El promedio de edad del género no binario es: {promedio_nb}')
#!D)
# Tecnologia con mas postulantes (solo hay una).
        alert('TP 07 - For', f'La tecnología con más postulantes es: {tecn_nombre_mas_postulantes}.')
#!E)
# Porcentaje de postulantes de cada genero.
        # alert('TP 07 - For', f'El porcentaje de postulantes masculinos es: {porcentaje_m}')
        # alert('TP 07 - For', f'El porcentaje de postulantes femeninos es: {porcentaje_f}')
        # alert('TP 07 - For', f'El porcentaje de postulantes no binarios es: {porcentaje_nb}')
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
