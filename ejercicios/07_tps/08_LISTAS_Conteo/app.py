import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.lista = [1,4,5]

    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True

        while flag_continuar:
            
            numero = prompt('TP 08 - Listas', 'Ingresa un número: ')
            
            numero = int(numero)
            self.lista.append(numero)

            
            flag_continuar = question('TP 08 - Listas','¿Desea continuar?')


    def btn_mostrar_estadisticas_on_click(self):
        flag_positivos = True
        flag_negativos = True
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros     = 0

        for numero in self.lista:
                if numero > 0:
                    contador_positivos += 1
                    acumulador_positivos += numero
                    if flag_positivos == True:
                        maximo_positivos = numero
                        flag_positivos = False
                    else:
                        if numero > maximo_positivos:
                            maximo_positivos = numero
                elif numero < 0:
                    contador_negativos += 1
                    acumulador_negativos += numero
                    if flag_negativos == True:
                        minimo_negativos = numero
                        flag_negativos = False
                    else:
                        if numero < minimo_negativos:
                            minimo_negativos = numero
                else:
                    contador_ceros += 1

        promedio_negativos = acumulador_negativos / contador_negativos

        # a. La suma acumulada de los negativos
        # b. La suma acumulada de los positivos
        alert('TP 08 - Listas', f'La suma acumulada de los negativos es {acumulador_negativos}, y la de los positivos es {acumulador_positivos}')
        # c. Cantidad de números positivos ingresados
        # d. Cantidad de números negativos ingresados
        # e. Cantidad de ceros
        alert('TP 08 - Listas', f'La cantidad de números negativos es: {contador_negativos}, de positivos es: {contador_positivos} y de ceros es: {contador_ceros}')
        # f. El minimo de los negativos
        # g. El maximo de los positivos
        alert('TP 08 - Listas', f'El mínimo de los negativos es: {minimo_negativos} y el máximo de los positivos es: {maximo_positivos}')
        # h. El promedio de los negativos
        alert('TP 08 - Listas', f'El promedio de los negativos es: {promedio_negativos}')


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
