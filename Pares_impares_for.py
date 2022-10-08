# Hacer el diagrama de flujo y programa en python, que lea 100 numeros enteros ( 3 o 4) y que averigue e imprima cuantos son pares y cuantos son impares 

print("\n-----------------------------------------------------------")
print("------- Programa para contar numeros pares e impares --------")
print("-----------------------------------------------------------\n")

#input
n=int(input("\nIngrese la cantidad de numeros a contar: "))

#processing
cont_pares=0
cont_impares=0

for i in range(n):
    num=int(input("\n ingrese el numero a evaluar: "))
    if(num%2)==0:
        cont_pares=cont_pares+1
    else:
        cont_impares=cont_impares+1
        
#output
print("\nLa cantidad de numeros pares es: "+str(cont_pares))
print("La cantidad de numeros impares es de: "+str(cont_impares))
print(" ")