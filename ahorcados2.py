import random

palabras = ["universo", "computadora", "papel", "lapiz", "borrador", "telefono", "teclado", "universidad", "programacion", "objeto"]

def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

def juego_ahorcado():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 5 
    ya_adivinadas = []

    print(f"La palabra tiene {len(palabra)} letras.")
    
    while intentos > 0:
        print("Palabra actual: ", mostrar_palabra(palabra, letras_adivinadas))
        print(f"Tiene {intentos} intentos restantes.")
        letra = input("Adivina una letra: ").lower()

        if letra in ya_adivinadas:
            print("Ya ha adivinado esa letra.")
            continue

        ya_adivinadas.append(letra)

        if letra in palabra:
            letras_adivinadas.append(letra)
        else:
            intentos -= 1
            print("Incorrecto")

        if all(letra in letras_adivinadas for letra in palabra):
            print("Ha adivinado la palabra:", palabra)
            break
    else:
        print("No hay más intentos. La palabra era:", palabra)

juego_ahorcado()
