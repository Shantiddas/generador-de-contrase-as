import random
import string
import tkinter as tk
from tkinter import messagebox

# Función para generar contraseñas
def generar_contraseña(longitud, incluir_letras, incluir_numeros, incluir_simbolos):
    caracteres = ""

    if incluir_letras:
        caracteres += string.ascii_letters  # Añade letras (mayúsculas y minúsculas)
    if incluir_numeros:
        caracteres += string.digits  # Añade números
    if incluir_simbolos:
        caracteres += string.punctuation  # Añade símbolos

    # Genera una contraseña aleatoria con la longitud especificada
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Función para obtener las entradas de la interfaz
def obtener_entradas():
    try:
        # Obtener la longitud de la contraseña desde el campo de entrada
        longitud = int(entry_longitud.get())

        # Obtener las opciones de incluir letras, números y símbolos
        incluir_letras = var_letras.get()
        incluir_numeros = var_numeros.get()
        incluir_simbolos = var_simbolos.get()

        # Verificar que al menos una opción esté seleccionada
        if not (incluir_letras or incluir_numeros or incluir_simbolos):
            messagebox.showerror("Error", "Debes seleccionar al menos una opción (letras, números o símbolos).")
            return

        # Generar la contraseña
        contraseña = generar_contraseña(longitud, incluir_letras, incluir_numeros, incluir_simbolos)

        # Mostrar la contraseña generada en la etiqueta
        label_resultado.config(text=f"Contraseña generada: {contraseña}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud de la contraseña.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x300")

# Título
label_titulo = tk.Label(ventana, text="Generador de Contraseñas", font=("Arial", 14))
label_titulo.pack(pady=10)

# Etiqueta para la longitud de la contraseña
label_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)

# Campo de entrada para la longitud de la contraseña
entry_longitud = tk.Entry(ventana)
entry_longitud.pack(pady=5)

# Opciones de incluir letras, números y símbolos
var_letras = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

# Casillas de verificación
checkbox_letras = tk.Checkbutton(ventana, text="Incluir letras", variable=var_letras)
checkbox_letras.pack()

checkbox_numeros = tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros)
checkbox_numeros.pack()

checkbox_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos)
checkbox_simbolos.pack()

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=obtener_entradas)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
label_resultado = tk.Label(ventana, text="Contraseña generada: ", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()

