print("Ingrese el monto total de la compra:")
monto_compra = float(input())

print("¿Es el cliente miembro VIP? (si/no):")
es_vip = input().lower()

if monto_compra >= 1000:
    descuento = 0.10  
    print("Se ha aplicado un descuento del 10% por la compra mayor o igual a $1,000.")
elif monto_compra >= 500:
    descuento = 0.05  
    print("Se ha aplicado un descuento del 5% por la compra mayor o igual a $500.")
else:
    descuento = 0.0  
    print("No se aplica descuento por compras menores a $500.")

total_con_descuento = monto_compra * (1 - descuento)

if es_vip == "si":
    total_con_descuento *= 0.95  
    print("Se ha aplicado un 5% adicional por ser cliente VIP.")

print(f"El total final a pagar es: ${total_con_descuento:.2f}")
