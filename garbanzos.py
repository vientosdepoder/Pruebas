num1 = float(input("Primer numero: "))
op = input("Operador: ")
num2 = float(input("Segundo nummero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("ERROR: Introduce un operador valido.")
