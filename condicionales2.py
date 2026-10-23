#Programa que me indica como me fue
calif=float(input("Dame tu calificasion"))
if calif==10:
    print("exelente!!!!")
elif calif==9:
    print("muy bien")
elif calif==8:
    print("bien")
elif calif==7:
    print("puedes mejorar")
elif calif==6:
    print("ay mijo")
else:
    print("chanclazooo")

#ahora de la temperatura
temp=float(input("dame la temperatura"))
if temp>=40:
    print("hace mucho calor")
elif temp>=30 and temp<40:
    print("esta templadito")
elif temp>=20 and temp<30:
    print("esta fresco")
elif temp>=10:
    print("hace frio")
else:
    print("no valido") 

#solicitar sexo tipo cadena =input()
#solicitar edad tipo entero=int(input())
sex=input("solicitar tu genero de sexo")
edad=int(input("ingresa tu edad"))
if sex=="hombre" and edad>=18:
    print("puede sacar cartilla militar")
else:
    print("no puedes")

