nombre=input("escribe nombre del empleado")
pagoHora=float(input("pago por  hora"))
horasMes=float(input("horas trabajadas al mes"))
sueldo=pagoHora*horasMes
bono= 0
if sueldo>=100 and sueldo <=300:
    bono=500
    print("tu sueldo es",sueldo+bono)
elif sueldo >300 and sueldo <=1500:
    bono=1700
    print("tu sueldo es",sueldo+bono)
elif sueldo >=1500 and sueldo <=3000:
    bono=3500
    print("tu sueldo es",sueldo+bono)
elif sueldo >3000 and sueldo <=8000:
    bono=8500
    print("tu sueldo es",sueldo+bono)
elif sueldo >8000: 
    bono=1000
    print("tu sueldo es",sueldo+bono)
else:
    mensajeBono= "no valido ms"


