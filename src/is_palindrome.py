def is_palindrome(texto):
    texto = texto.lower()
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'ñ': 'n'
    }

    texto_limpio = []
    for caracter in texto:
        if caracter in reemplazos:
            texto_limpio.append(reemplazos[caracter])
        elif caracter.isalnum():
            texto_limpio.append(caracter)

    texto_final = ''.join(texto_limpio)
    return texto_final == texto_final[::-1]

# Entrada y salida
entrada = input("Ingrese una palabra o frase: ")
if is_palindrome(entrada):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

