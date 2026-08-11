###
# 03 - range()
# Permite generar una secuencia de números enteros, que se puede utilizar para iterar sobre un bucle.
###

print( "\nRange: " )
nums = range( 5 ) #Genera una secuencia de números del 0 al 4

#for num in nums:
    #print( "Número: ", num )


for num in range( 5, 10 ): #Genera una secuencia de números del 5 al 9
    print( "Número: ", num )

#range( start, stop, step ) #Genera una secuencia de números desde start hasta stop-1, con un paso de step
for num in range( 0, 10, 2 ): #Genera una secuencia de números del 0 al 9, con un paso de 2
    print( "Número: ", num )

for num in range( -5, 0 ): #Genera una secuencia de números del -5 al -1
    print( "Número: ", num )

for num in range( 10, 0, -1 ): #Genera una secuencia de números del 10 al 1
    print( "Número: ", num )

for num in range( 0,444):
    print(num)

nums = range( 0, 10 )
lista = list( nums ) #Convierte la secuencia de números en una lista
print( "Lista: ", lista )

for _ in range( 5 ): #El guion bajo es una convención para indicar que no se va a utilizar la variable
    print( "Hola" )
