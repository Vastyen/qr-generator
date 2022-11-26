# Importación de librerías
import customtkinter
import tkinter 
import qrcode
import os
import mysql.connector
from tkinter import messagebox

# Conexión con bases de datos.
mydb = mysql.connector.connect(
    host="localhost",
    user="App",
    port="3306",
    password="App",
    database="App"
)

# Se verifica la existencia de la tabla.
check = 0
mycursor = mydb.cursor()
mycursor.execute("Show tables;")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    print(check)
    if x[0] == "listaInvitados":
        check = check+1

# En caso de no existir la tabla, se crea.
if check == 0:
    mycursor.execute("CREATE TABLE listaInvitados (invitado_id int AUTO_INCREMENT PRIMARY KEY, nombrePersonal VARCHAR(255), rutPersonal VARCHAR(255), nombreEmpresa VARCHAR(255), rutEmpresa VARCHAR(255), motivoVisita VARCHAR(255), fechaVisita VARCHAR(255), ventanaVisita VARCHAR(255))")
    print("Tabla creada")

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


# Título 
text_var = tkinter.StringVar(value="Control de Acceso QR")
titulo = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=120,
                               height=20,
                               text_font=("Arial", 45),
                               corner_radius=8)
titulo.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

# Autores
autores = customtkinter.CTkLabel(master=app, text="Desarrollado por Bastián Escribano")
autores.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Entradas del Formulario
entryNombrePersonal = customtkinter.CTkEntry(
    master=app, placeholder_text="Nombre del Personal")
entryNombrePersonal.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

entryRut = customtkinter.CTkEntry(
    master=app, placeholder_text="Rut del Personal")
entryRut.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

entryNombreEmpresa = customtkinter.CTkEntry(
    master=app, placeholder_text="Nombre de Empresa")
entryNombreEmpresa.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)

entryRutEmpresa = customtkinter.CTkEntry(
    master=app, placeholder_text="Rut de Empresa")
entryRutEmpresa.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

entryMotivoVisita = customtkinter.CTkEntry(
    master=app, placeholder_text="Motivo de Visita")
entryMotivoVisita.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)

entryFechaVisita = customtkinter.CTkEntry(
    master=app, placeholder_text="Fecha de Visita")
entryFechaVisita.place(relx=0.7, rely=0.3, anchor=tkinter.CENTER)

entryVentanaTiempo = customtkinter.CTkEntry(
    master=app, placeholder_text="Ventana de Tiempo")
entryVentanaTiempo.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)

# Función que crea el código QR y además inserta los datos a la base de datos
def controlador():

    text1 = entryNombrePersonal.get()
    text2 = entryRut.get()
    text3 = entryNombreEmpresa.get()
    text4 = entryRutEmpresa.get()
    text5 = entryMotivoVisita.get()
    text6 = entryFechaVisita.get()
    text7 = entryVentanaTiempo.get()

    # Validación para las entradas de texto del formulario.

    if text1 != "" and text2 != "" and text3 != "" and text4 != "" and text5 != "" and text6 != "" and text7 != "":

        sql = "INSERT INTO listaInvitados (nombrePersonal, rutPersonal, nombreEmpresa, rutEmpresa, motivoVisita, fechaVisita, ventanaVisita) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (text1, text2, text3, text4, text5, text6, text7)
        mycursor.execute(sql, val)
        mydb.commit()
        qrObject = {
            "Nombre Personal": text1,
            "Rut Personal": text2,
            "Nombre Empresa": text3,
            "Rut Empresa": text4,
            "Motivo Visita": text5,
            "Fecha Visita": text6,
            "Ventana de Tiempo": text7
        }

        img = qrcode.make(qrObject)
        type(img)  
        img.save("src/qr.png")
        os.system("python3 src/QR.py")
    else:
        messagebox.showinfo(
            message="Debe llenar todos los campos.", title="Alerta de Control de Acceso QR")

# Botón que genera el código QR e inserta los datos a la base de datos.
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Generar Código QR",
                                 command=controlador)
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()
