from io import open


def Ejercicio2():
    archivo_texto = open("archivo_texto.txt","r+")


    i = int(input("digite la cantidad de líneas que desee que tenga su archivo de texto: "))

    if (i>0):

        for j in range(1,i+1,1):
            word = input(f"Digite la que cadena que desea guardar en la línea {j}: ")
            archivo_texto.write(word+ '\n') 

    else:
        print("la cantidad de líneas debe ser mayor que cero")

    lista_de_lineas = archivo_texto.readlines()

    print(f"Arhivo Guardado con éxito. \n El arhivo contiene lo siguiente: \n {lista_de_lineas}")


    archivo_texto.close()


def Ejercicio2Testeado():
    correcto = False
    while (not correcto):
        try:
            Ejercicio2()
            correcto = True
        except ValueError:
            print("la cantidad ingresada debe ser de tipo numérica")


Ejercicio2Testeado()
            

