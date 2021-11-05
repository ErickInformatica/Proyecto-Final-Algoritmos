# Programa para poder editar documentos de textos sin importar la extension.
# Fecha: 05/11/2021
# Autor: Erick Bran
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk,Image  

def browseFile():
    global nombreArchivo
    nombreArchivo = filedialog.askopenfilename(initialdir="/", title="Selecciona una archivo", filetype=(("Todos los archivos", "*.*"),))
    label_exploradorArchivos.configure(text="Archivo Abierto: "+nombreArchivo)
    file = open(nombreArchivo, 'r')
    content = file.read()
    archivoTexto.insert(END, content)
    labelGuardado.configure(text="")

def guardar():
    inputData = archivoTexto.get("1.0", "end-1c")
    fileout = open(nombreArchivo, 'w')
    fileout.write(inputData)
    fileout.close()
    archivoTexto.delete('1.0', END)
    label_exploradorArchivos.configure(text="") 
    labelGuardado.configure(text="Archivo Guardado", foreground="blue")   
    labelGuardado.pack()

def datos():
    nuevaVentana = Toplevel(ventanaPrincipal)
    nuevaVentana.title("Datos Personales")
    nuevaVentana.geometry("400x200")
    Label(nuevaVentana, text="Mis datos").pack()

    logoUMG = Image.open("C:/Users/ebran/Pictures/umg-logo.png") #Esta direccion debe ser en base a donde se encuentre la imagen de lo contrario no mostrara nada.
    logoUMG = logoUMG.resize((100, 89), Image.ANTIALIAS)
    cargaImagen = ImageTk.PhotoImage(logoUMG)
    img = Label(nuevaVentana, image=cargaImagen)
    img.image = cargaImagen
    img.place(x=0, y=0)
    Label(nuevaVentana, text="Autor: Erick Daniel Bran Enriquez").pack()
    Label(nuevaVentana, text="Carné: 7690-21-11260").pack()


ventanaPrincipal = Tk()
ventanaPrincipal.geometry("750x500")
ventanaPrincipal.title("Editor de Archivos")


labelGuardado = Label(ventanaPrincipal)
label_exploradorArchivos = Label(ventanaPrincipal, text="Seleccionador de Archivos", anchor=CENTER)
button_exploradorAchivos = Button(ventanaPrincipal, text="Buscar Archivo", command=browseFile)
button_exit = Button(ventanaPrincipal, text="Salir", command=exit)

button_guardar = Button(ventanaPrincipal, text="Guardar", command=guardar)
button_datos = Button(ventanaPrincipal, text="Datos", command=datos)

frame =  Frame(ventanaPrincipal)
scroll = Scrollbar(frame, orient=VERTICAL)

archivoTexto = Text(frame, height = 5, width = 52, yscrollcommand=scroll.set)
scroll.config(command=archivoTexto.yview)
scroll.pack(side=RIGHT, fill=Y)

label_exploradorArchivos.pack()
button_exploradorAchivos.pack()
button_exit.pack()
archivoTexto.pack(expand=True, fill=BOTH, side=LEFT)
frame.pack(expand=True, fill=BOTH, padx=20, pady=20)
button_guardar.pack()
button_datos.pack()
ventanaPrincipal.mainloop()