peso = float(input("Ingresa una cantidad en pesos: "))
dolar = float(input("Ingresa el precio del dólar: "))

conversion = peso / dolar

print(f"{peso} pesos equivalen a {conversion:.2f} dólares.")