from secrets import choice
caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
longitud = 10
# La longitud que queremos
cadena_aleatoria = ''.join(choice(caracteres) for caracter in range(longitud))
print("La cadena es: ", cadena_aleatoria)
#no.
print("loquequiera")
