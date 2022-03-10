import random



n= 100
pe= 0

a= [None]*n 
b= [None]*n

print("Ejercicio 2.3 parte 3")
for i in range(0,n):
    a[i] = random.randint(0,1)
    b[i] = random.randint(0,1)

print("Lista numero 1: ",a)
print("")
print("Lista numero 2:",b)
print("")

for i in range(0,n):
    pe = pe + a[i] * b[i]

print("El producto escalar de a y b es: ",pe)