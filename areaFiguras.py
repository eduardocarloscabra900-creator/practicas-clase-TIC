#programa para calcular area
#Area cuadrado; lado x lado 
lado=float(input("ingresa lado"))
areaCuadrado=lado*lado
print("el area es", areaCuadrado)
print(f'el area es {areaCuadrado}')
#Area de un triangulo (base x altura)/2
base=float(input("ingresa la base"))
altura=float(input("ingresa la altura"))
areaTriangulo=(base*altura)/2
print("el area es",{areaTriangulo})
#Area de un trapecio
baseM=float(input("ingresa baseM"))
base=float(input('ingresa altura'))
areaTrapecio= (baseM+base)/2 *altura
print("el area del trapecio es",{areaTrapecio})
