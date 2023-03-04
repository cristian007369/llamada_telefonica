#Programa para calcular el costo de una llamada

print("-------------------------------------")
print("---------------llamada---------------")
print("-------------------------------------")

#Input

tl=int(input("Ingrese la duración de la llamada en MINUTOS, los segundos no los TENGA EN CUENTA: "))

#Processing y output

if tl<=3:
    print("-------------------------------------")
    print("El costo de la llamada es de 300$")
    print("-------------------------------------")
else:
    x=(tl-3)*50+300
    print("-------------------------------------")
    print("El costo de la llamada es de " + str(x)+"$")
    print("-------------------------------------")