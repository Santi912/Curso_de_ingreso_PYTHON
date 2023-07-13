import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad     = self.combobox_cantidad.get()
        cantidad     = int(cantidad)
        marca        = self.combobox_marca.get()
        precio_total = 0
        precio_sin_descuento = 800 * cantidad

        #A)
        if cantidad >= 6: 
            descuento = 50

        #B)
        elif cantidad == 5:
            if marca == 'ArgentinaLuz':
                descuento = 40
            else:
                descuento = 30
        
        #C)
        elif cantidad == 4:
            if marca == 'ArgentinaLuz' or marca == 'FelipeLamparas':
                descuento = 25
            else: 
                descuento = 20

        #D)
        elif cantidad == 3: 
            if marca == 'ArgentinaLuz':
                descuento = 15
            elif marca == 'FelipeLamparas':
                descuento = 10
            else:
                descuento = 5
        
        #Este cálculo va aca xq sino no podremos hacer el próximo, en el que varía la formula.
        precio_total = precio_sin_descuento - precio_sin_descuento * (descuento / 100)
        
        #E)
        if precio_total >= 4000:
            descuento = 5
            precio_total = precio_total - precio_total * (descuento / 100)
                    #Aqui, para que sea ADICIONAL, debemos restar del precio total, no el sin_descuento

        #Con esta formula, y gracias a diferenciar (al principio) el precio_total, precio_sin_descuento y descuento, puedo obtener el precio final solo escribiendo el descuento explicitamente.
        # Debe ir aca debajo xq asi el if cambia el valor de descuento (descuento / 100 da 0.*el porcentaje requerido*)
        mensaje = f'El total de la compra es: ${precio_total}.'       
        alert('TP 04 - FerreteIluminaria', mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()