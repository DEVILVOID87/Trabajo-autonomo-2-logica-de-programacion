import random
import string
import os

# ==========================================
# PROYECTO INTEGRADOR (INDIVIDUAL)
# El impacto de las nuevas tecnologías en la sociedad:
# visualización del futuro (CIBERSEGURIDAD)
# ==========================================

MIN_LONGITUD = 8

# Conjuntos de caracteres
LETRASMAY = string.ascii_uppercase
LETRASMIN = string.ascii_lowercase
NUMEROS = string.digits
SIMBOLOS = "!@#$%^&*="

# 1 GENERAR CONTRASEÑA

def pedir_longitud():
    while True:
        try:
            longitud = int(input(f"Ingrese la longitud (mínimo {MIN_LONGITUD}): "))
            if longitud >= MIN_LONGITUD:
                return longitud
            else:
                print(f"La longitud mínima permitida es {MIN_LONGITUD}. Intente nuevamente.\n")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.\n")


def generar_contrasena(longitud):
    password = ""
    contador = 0

    while contador < longitud:
        tipo = random.randint(1, 4)

        if tipo == 1:
            caracter = random.choice(LETRASMAY)
        elif tipo == 2:
            caracter = random.choice(LETRASMIN)
        elif tipo == 3:
            caracter = random.choice(NUMEROS)
        else:
            caracter = random.choice(SIMBOLOS)

        password += caracter
        contador += 1

    return password

# 2 EVALUAR SEGURIDAD

def evaluar_contrasena(password):
    puntos = 0

    if len(password) >= 12:
        puntos += 2
    elif len(password) >= 8:
        puntos += 1

    if any(c.isupper() for c in password):
        puntos += 1
    if any(c.islower() for c in password):
        puntos += 1
    if any(c.isdigit() for c in password):
        puntos += 1
    if any(c in SIMBOLOS for c in password):
        puntos += 1

    if puntos <= 2:
        nivel = "BAJO"
    elif puntos <= 4:
        nivel = "MEDIO"
    else:
        nivel = "ALTO"

    return puntos, nivel

# 3 VISUALIZACIÓN DEL FUTURO

def visualizar_futuro(nivel, adopcion):
    if nivel == "BAJO":
        riesgo = "ALTO"
        impacto = "Alta probabilidad de robo de cuentas, fraudes y pérdida de privacidad."
    elif nivel == "MEDIO":
        riesgo = "MEDIO"
        impacto = "Riesgo moderado; algunos ataques pueden evitarse."
    else:
        riesgo = "BAJO"
        impacto = "Menor riesgo de hackeos y mejor protección de datos personales."

    if adopcion == "alta":
        escenario = (
            "Para 2030, el aumento del uso de tecnologías y ataques automatizados "
            "hará que las contraseñas débiles sean fácilmente vulneradas."
        )
    elif adopcion == "media":
        escenario = (
            "Para 2030, habrá mayor concientización sobre seguridad digital, "
            "aunque seguirán existiendo riesgos."
        )
    else:
        escenario = (
            "Para 2030, el bajo avance tecnológico mantendrá riesgos asociados "
            "al desconocimiento y malas prácticas."
        )

    return (
        f"Riesgo: {riesgo}\n"
        f"Impacto social: {impacto}\n"
        f"Escenario futuro: {escenario}"
    )

# 4 EXPORTAR REPORTE

def exportar_reporte(password, puntos, nivel, adopcion, futuro_texto):
    os.makedirs("docs", exist_ok=True)

    contenido = ""
    contenido += "PROYECTO INTEGRADOR\n"
    contenido += "El impacto de las nuevas tecnologías en la sociedad: visualización del futuro\n"
    contenido += "Tema: Ciberseguridad y contraseñas seguras\n"
    contenido += "------------------------------------------------------------\n"
    contenido += f"Contraseña: {password}\n"
    contenido += f"Longitud: {len(password)}\n"
    contenido += f"Puntaje: {puntos}\n"
    contenido += f"Nivel de seguridad: {nivel}\n"
    contenido += f"Adopción tecnológica: {adopcion}\n"
    contenido += "------------------------------------------------------------\n"
    contenido += "VISUALIZACIÓN DEL FUTURO:\n"
    contenido += futuro_texto + "\n"

    ruta = os.path.join("docs", "reporte_proyecto.txt")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

    return ruta

# MODO CONSOLA

def ejecutar_consola():
    ultima_contrasena = ""
    ultimo_puntaje = 0
    ultimo_nivel = ""
    ultimo_futuro = ""
    ultima_adopcion = ""

    while True:
        print("\n1) Generar contraseña")
        print("2) Evaluar seguridad")
        print("3) Visualizar futuro")
        print("4) Exportar reporte")
        print("0) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            longitud = pedir_longitud()
            ultima_contrasena = generar_contrasena(longitud)
            print("Contraseña generada:", ultima_contrasena)

        elif opcion == "2":
            if ultima_contrasena == "":
                ultima_contrasena = input("Ingrese una contraseña: ")
            ultimo_puntaje, ultimo_nivel = evaluar_contrasena(ultima_contrasena)
            print("Puntaje:", ultimo_puntaje)
            print("Nivel:", ultimo_nivel)

        elif opcion == "3":
            if ultimo_nivel == "":
                print("Primero evalúe una contraseña.")
                continue
            ultima_adopcion = input("Adopción tecnológica (baja/media/alta): ").lower()
            ultimo_futuro = visualizar_futuro(ultimo_nivel, ultima_adopcion)
            print(ultimo_futuro)

        elif opcion == "4":
            if ultima_contrasena == "" or ultimo_futuro == "":
                print("Debe completar los pasos anteriores.")
                continue
            ruta = exportar_reporte(
                ultima_contrasena,
                ultimo_puntaje,
                ultimo_nivel,
                ultima_adopcion,
                ultimo_futuro
            )
            print("Reporte guardado en:", ruta)

        elif opcion == "0":
            break

        else:
            print("Opción no válida.")

# MODO INTERFAZ GRAFICA

def ejecutar_interfaz():
    import tkinter as tk
    from tkinter import messagebox

    password = ""
    nivel = ""
    puntos = 0
    futuro = ""

    def generar():
        nonlocal password
        try:
            longitud = int(entry_longitud.get())
            if longitud < MIN_LONGITUD:
                messagebox.showwarning("Aviso", "La longitud mínima es 8.")
                    def generar():
        nonlocal password
        try:
            longitud = int(entry_longitud.get())
            if longitud < MIN_LONGITUD:
                messagebox.showwarning("Aviso", "La longitud mínima es 8.")
                return
        except ValueError:
            messagebox.showwarning("Aviso", "Ingrese un número válido.")
            return

        password = generar_contrasena(longitud)
        lbl_password.config(text=password)
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, "Contraseña generada.\n")

    def evaluar():
        nonlocal puntos, nivel
        if password == "":
            messagebox.showwarning("Aviso", "Primero genere una contraseña.")
            return
        puntos, nivel = evaluar_contrasena(password)
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, f"Puntaje: {puntos}\nNivel: {nivel}\n")

    def ver_futuro():
        nonlocal futuro
        if nivel == "":
            messagebox.showwarning("Aviso", "Primero evalúe la contraseña.")
            return
        adopcion = var_adopcion.get()
        futuro = visualizar_futuro(nivel, adopcion)
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, futuro)

    def exportar():
        if password == "" or nivel == "" or futuro == "":
            messagebox.showwarning("Aviso", "Genere, evalúe y visualice el futuro antes de exportar.")
            return
        ruta = exportar_reporte(password, puntos, nivel, var_adopcion.get(), futuro)
        messagebox.showinfo("Listo", f"Reporte guardado en:\n{ruta}")

    ventana = tk.Tk()
    ventana.title("Proyecto Integrador - Ciberseguridad")
    ventana.geometry("520x430")

    tk.Label(ventana, text="Longitud de la contraseña (mínimo 8):").pack()
    entry_longitud = tk.Entry(ventana)
    entry_longitud.pack()

    tk.Button(ventana, text="Generar contraseña", command=generar).pack(pady=5)

    tk.Label(ventana, text="Contraseña:").pack()
    lbl_password = tk.Label(ventana, text="", fg="blue")
    lbl_password.pack()

    tk.Button(ventana, text="Evaluar seguridad", command=evaluar).pack(pady=5)

    tk.Label(ventana, text="Adopción tecnológica:").pack()
    var_adopcion = tk.StringVar(value="media")
    tk.OptionMenu(ventana, var_adopcion, "baja", "media", "alta").pack()

    tk.Button(ventana, text="Visualizar futuro", command=ver_futuro).pack(pady=5)
    tk.Button(ventana, text="Exportar reporte", command=exportar).pack(pady=5)

    tk.Label(ventana, text="Resultados:").pack()
    txt_resultado = tk.Text(ventana, height=10, width=60)
    txt_resultado.pack(pady=5)

    ventana.mainloop()

def main():
    print("Seleccione el modo de ejecución:")
    print("1) Consola")
    print("2) Interfaz gráfica")
    opcion = input("Opción: ").strip()

    if opcion == "2":
        ejecutar_interfaz()
    else:
        ejecutar_consola()

if __name__ == "__main__":
    main()
