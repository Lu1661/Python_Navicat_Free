from IMPORTACION import ejecutar_script
import tkinter as tk

ventanacolor = "#000000"  # Negro para el fondo
labelcolor = "#FF0000"   # Rojo brillante para las etiquetas
labelletracolor = "#FFFFF0" # Casi blanco para el texto, para contraste
botoncolor = "#FFD700"   # Oro para los botones, complementando el esquema
botonletracolor = "#8B0000" # Rojo oscuro para el texto de los botones

Fuente_Label = ("Calibri",10)
Fuente_Button = ("Calibri",10)

ventana = tk.Tk()
ventana.title("THUNDER CAT")
ventana.config(bg=ventanacolor)
ventana.geometry("320x40")
ventana.resizable(0, 0)
ventana.iconbitmap("C:/Ingresa/tuRuta/Aqui/RAYO_GATO.ico")

etiqueta1 = tk.Label(ventana, text="ACT. NAVICAT", bg=labelcolor, fg=labelletracolor, font=Fuente_Label, width=20, height=1)
etiqueta1.grid(row=0, column=0, padx=5, pady=5)
boton1 = tk.Button(ventana, text="RUN", command=ejecutar_script, bg=botoncolor, fg=botonletracolor, width=20, height=1)
boton1.grid(row=0, column=1, padx=5, pady=5)

ventana.mainloop()