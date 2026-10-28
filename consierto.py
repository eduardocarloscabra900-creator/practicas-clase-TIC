edad=int(input("edad:"))
permiso=input("¿tienes permiso de tus padres?")
acompañado=input("¿vas acompañado?")
if edad >=18 or permiso=="si":
    print("puedes entrar al concierto")
elif edad >=18 or acompañado =="si":
    print("puedes entrar al consierto")
else:
    print("no puedes entrar al concierto")