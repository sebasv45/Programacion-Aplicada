LISTAS Y TUPLAS
##############LISTAS##############
##################################



my_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde'] #
#input
print(my_lista)
print(type(my_lista))
print(my_lista[2])


print('my_lista size:', len(my_lista))
print(my_lista[0:2])
print(my_lista[:2])

my_lista.append('Blanco')    #Agrega elemento Blanco al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')  #Agrega el elemento Negro en la lista
print(my_lista)

my_lista.extend(['Marron','Gris'])  #Concatena otra lista
print(my_lista)


print(my_lista.index('Azul')) #Muestra en posicion de la lista se encuentra el elemento

#my_lista.remove('Magenta')
my_lista.remove('Marron') #Elimina el elemento Marron de la lista
print(my_lista)

my_lista.insert(7,'Marron') #Agrega el elemento Marron en la posicion 8 de la lista
print(my_lista)

print(my_lista.pop()) #Muestra el ultimo valor de la lista
size = len(my_lista)
print('size =',size) #Muestra el largo de la lista
#print(my_lista.pop(size))


my_lista_3 = my_lista * 3
print('my_lista_3',my_lista_3) #Muestra 3 veces my_lista


print('Sort:')
print()
my_listaSort = my_lista.sort()
print(my_listaSort)

my_NumList = [10,9,8,7,6,5,4,3,2,1]
print('Ordering my_NumList')
my_NumList.sort() # Ayuda a organizar la lista de numeros de menor a mayor
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor

my_NumList.sort(reverse = True) # Ya que se esta utilizando el comando sort en my_NumList cuando usamos reverse estariamos organizando
                                # la lista de mayor a menor
print('De menor a mayor:', my_NumList)


###############UPLAS##############
##################################

# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables


#Convertir una lista a tupla:prin

print('#####################')
print('#####################')
print('#####################')
print('#####################')
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ",my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)

print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar' , 5,8,1999
print(my_tupla)


#Desempaquetado de tupla, se guardan los valores en orden de las variables}
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print('Nombre: ',nombre, ' -Dia:',dia,'-Mes: ', mes, '-Año: ',año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
