'''
Created on Nov 4, 2017

@author: vagrant
'''


def Mostrarproductos(matriz):
    for a in range(0,len(matriz[0])):
        print(str(a)+"-> "+matriz[0][a]+" -  $"+str(matriz[1][a]))   
        
productos = [["Yerba","Merc","Asado","Corchos","Comida"],[55,438,230,8,96]]

Mostrarproductos(productos)

ticket = [[],[],[]]

termina = 'no'

Mostrarproductos(productos)

while termina == 'no':
    
    codigo = input("ingresar codigo de articulo")
    cantidad = input ("ingresar cantidad")
    ticket[0].append(int(cantidad))
    ticket[1].append(int(codigo))
    ticket[2].append(int(cantidad))
    termina = input("termina? si/no")