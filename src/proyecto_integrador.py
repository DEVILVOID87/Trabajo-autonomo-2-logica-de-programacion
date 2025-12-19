import random

def generar_contrasena_segura():
    # Inicialización de conjuntos de caracteres
    LETRASMAY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LETRASMIN = "abcdefghijklmnopqrstuvwxyz"
    NUMEROS = "0123456789"
    SIMBOLOS = "!@#$%^&*="
    
    MIN_LONGITUD = 8

    # Bienvenida
    print("**Bienvenido al Sistema de Generación Seguro de Contraseñas**\n")

    # Validación de la longitud de la contraseña
    while True:
        try:
            # Entrada del usuario (GET longitud)
            longitud = int(input(f"Ingrese los caracteres para su contraseña (mínimo {MIN_LONGITUD} caracteres): "))
            
            # Condición de salida del bucle (longitud >= MIN_LONGITUD)
            if longitud >= MIN_LONGITUD:
                break
            else:
                # Mensaje de error (PUT)
                print(f"Los caracteres permitidos mínimos son {MIN_LONGITUD}. Ingrese nuevamente.\n")
        except ValueError:
            # Manejo de entrada no numérica
            print("Entrada no válida. Por favor, ingrese un número entero.\n")
            
    # Inicialización de variables para la generación
    password = ""
    contador = 0

    # Bucle principal de generación de contraseña
    while contador < longitud:
        # Generar un tipo de caracter aleatorio (1, 2, 3 o 4)
        # FLOOR(RANDOM * 4) + 1  se traduce a random.randint(1, 4) en Python
        tipo = random.randint(1, 4) 
        
        caracter = ''
        
        if tipo == 1: # Letra Mayúscula
            # index ← FLOOR(RANDOM * 26) + 1 (Índice de 1 a 26)
            # En Python, el índice va de 0 a 25.
            index = random.randint(0, len(LETRASMAY) - 1)
            caracter = LETRASMAY[index]
            
        elif tipo == 2: # Letra Minúscula
            index = random.randint(0, len(LETRASMIN) - 1)
            caracter = LETRASMIN[index]
            
        elif tipo == 3: # Número
            index = random.randint(0, len(NUMEROS) - 1)
            caracter = NUMEROS[index]
            
        elif tipo == 4: # Símbolo
            index = random.randint(0, len(SIMBOLOS) - 1)
            caracter = SIMBOLOS[index]
            
        # Concatenar caracter
        password += caracter
        # Incrementar contador
        contador += 1
    
    # Salida de resultados y finalización
    print("\nLa contraseña generada es:")
    print(password)
    print("\n¡Gracias por usar el generador! ¡Hasta pronto!")

# Ejecutar la función
generar_contrasena_segura()
