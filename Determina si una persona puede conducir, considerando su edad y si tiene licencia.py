print("Ingrese la edad de la persona:")
edad = int(input())

# Mayor de edad
if edad >= 18:
    print("La persona es mayor de edad.")
    
    # Tiene licencia ?
    print("¿Tiene licencia de conducir? (si/no):")
    licencia = input().lower()
    
    if licencia == "si":
        print("La persona puede conducir.")
    else:
        print("La persona no puede conducir porque no tiene licencia.")
else:
    print("La persona no es mayor de edad y no puede conducir.")
