#Garbanzos V0.1
#se parte de la versión cruda y se implementas funciones ingresar y opera

def ingresar(etiqueta):
#en el futuro esta función debería manejar el ingreso de numeros imaginarios, vectores, matrices y cualquier otro operando
#mostrar la etiqueta , pedir confirmacion
    valor = float(input(etiqueta))
    return valor

def opera(*args): #(operador,numero1,numero2,numero3,....)
#recibe un numero desconocido de parametros '*' que se acceden como args[0] el primero, args[1] el segundo....
    op=args[0]

    if op == "+":
        print(args[1] + args[2])
    elif op == "-":
        print(args[1]- args[2])
    elif op == "/":
        print(args[1] /args[2])
    elif op == "*":
        print(args[1] * args[2])
    else:
        print("ERROR: Introduce un operador valido.")


num1 = ingresar("Primer numero: ")
operador = input("Operadora: ")
num2 = ingresar ("Segundo nummero: ")


opera(operador,num1,num2)
