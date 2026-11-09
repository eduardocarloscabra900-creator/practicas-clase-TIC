#programa que agrege peliculas a una lista 
#ponerle nombre a mi lista
peliculas=[]
#pregunta cuantas pelis
cantidadPelis=int(input("cuantas peliculas vas a agragar"))
#valor inicial para el while
i=0
#mientras i sea menor a cantidad ejecuta
while i<cantidadPelis:
    print("hola")
    #preguntar pleiculas
    peli=input("ingresa peli: ")
    #agrega peliculas ala lista
    print(peliculas)
    i=i+1 
    peliBuscar=input("quepeli buscas")
    if peliBuscar in peliculas:
        print("si estas")
else:
    print("no esta pero dejame la agrago")
    peliculas.append(peliBuscar)
    print(peliculas)
    #lo extra
    peliBorrar=input("que pelicula quieres borrar:")
    peliculas.remove(peliBorrar)
    print(peliculas)