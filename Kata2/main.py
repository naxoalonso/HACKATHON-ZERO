precio = 3.49
decuento = 1 - 0.6
precio_con_descuento = precio * descuento 

numero_de_barras = input ("Numero de barras vendiadas: ")

print ("Precio habitual " + str(precio))
print ("descuento "+ str(precio_con_descuento))
print("Coste final: " +str(numero_de_barras * precio_con_descuento))