sexo=input("sexo= mujer o hombre")
edad=int(input("edad"))
estadoCibil=input(("estado cibil (soltera,casada,etc)"))
hijos=int(input("cantidad de hijos"))
if sexo=="mujer" and hijos==1 and edad <18:
    print("eres mujer, tines un hijo eres menor de edadel apoyo sera de $800")
elif sexo=="mujer" and hijos==1 and edad >=18:
    print("eres mujer, tienes un hijo y eres mayor de edad entonces el apoyo sera de $300")
elif sexo=="mujer" and hijos >1 and edad >18:
    print("eres mujer; tienes mas de un hijo y eres menor de edad entonces el apoyo es de $1500")
elif sexo=="mujer" and hijos >1 and edad >=18:
    print("eres mujer, tienes mas de un hijo y ya eres mayor de edad entonces el apoyo es de $500")
elif sexo== "hombre" and hijos >=1 and estadoCibil == "soltero":
    print("eres hombre y tienes hijos el apoyo es de $780")
else:
    print("no valido")