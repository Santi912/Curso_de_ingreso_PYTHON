'''
Nombre: Santiago
Apellido: Decibe
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        flag_continuar = True
        flag_primero   = True
        acumulador_candidatos = 0
        acumulador_edades   = 0
        total_votos = 0

        while flag_continuar == True:
            acumulador_candidatos += 1

            candidato = prompt('TP 06 - While', 'Ingrese el nombre del candidato: ')
            while candidato.isdigit() or candidato == '':
                candidato = prompt('TP 06 - While', 'Ingrese el nombre del candidato: ')
            
            edad_candidato = prompt('TP 06 - While', 'Ingrese la edad del candidato: ')
            while edad_candidato.isdigit() == False or int(edad_candidato) > 120:
                edad_candidato = prompt('TP 06 - While', 'Ingrese la edad del candidato: ')
            edad_candidato = int(edad_candidato)

            votos_candidato = prompt('TP 06 - While', '¿Cuántos votos recibió?')
            while votos_candidato.isdigit() == False or int(votos_candidato) < 0 or votos_candidato == None:
                votos_candidato = prompt('TP 06 - While', '¿Cuántos votos recibió?')
            votos_candidato = int(votos_candidato)
                
            #candidato con mas y menos votos
            if flag_primero == True:
                mas_votos    = votos_candidato
                menos_votos  = votos_candidato
                msj_mas_votos    = candidato
                msj_menos_votos  = candidato
                edad_menos_votos = edad_candidato
                flag_primero = False
            else:
                if votos_candidato > mas_votos:
                    mas_votos = votos_candidato
                    msj_mas_votos = candidato
                elif votos_candidato < menos_votos:
                    edad_menos_votos = edad_candidato
                    msj_menos_votos  = candidato

            #total votos
            total_votos += votos_candidato

            #acumulador edades
            acumulador_edades += edad_candidato
                
            flag_continuar = question('TP 06 - While','¿Desea continuar?')

        #promedio edades
        promedio = acumulador_edades / acumulador_candidatos
        alert('TP 06 - While', f'El promedio de las edades es {promedio}.')

        #nombre mas votos
        alert('TP 06 - While',f'El candidato con más votos es: {msj_mas_votos}')

        #nombre y edad menos votos
        alert('TP 06 - While',f'El candidato con menos votos es: {msj_menos_votos}, que tiene {edad_menos_votos}')

        #total votos emitidos
        alert('TP 06 - While', f'El total de los votos emitidos es: {total_votos}')


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
