# Importación de librerías
import customtkinter
import tkinter

# Modes: Sistema (default)
customtkinter.set_appearance_mode("System")
# Themes: Azul (default)
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # Se crea la aplicación de Tkinter.
app.title("Control de Acceso QR")
app.resizable(False, False)

# Parámetros de lanzamiento de la aplicación
width = 600  # Ancho 
height = 600  # Largo
screen_width = app.winfo_screenwidth()  # Ancho de la pantalla
screen_height = app.winfo_screenheight()  # Alto de la pantalla
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

# La aplicación se inicia en medio de la pantalla
app.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Se abre la imagen del código QR.
imagen = tkinter.PhotoImage(file="src/qr.png")

#Se muestra el código QR en ventana.
tkinter.Label(app, image=imagen).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
