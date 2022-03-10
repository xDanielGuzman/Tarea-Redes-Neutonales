from pickle import NONE
import random

n=3
pe = 0

a = [None]*n
b = [None]*n

print ("Ejercicio 2a)")

for i in range (0,n):
    a[i] = random.randint(0,1)
    b[i] = random.randint(0,1)

print("Lista numero 1:",a)
print("")
print("Lista numero 1:",b)
print("")

for i in range(0,n):
    pe = pe + a[i] * b[i]

print("El producto escalar de a y b es: ",pe)