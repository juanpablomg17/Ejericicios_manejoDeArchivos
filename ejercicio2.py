from io import open

#MÉTODO PARA ESCRIBIR LÍNEAS DE TEXTO EN N CADENAS DIFERENTES
def EscribirLineasDeTexto():
    archivo_texto = open("archivo_texto.txt","a")


    i = int(input("digite la cantidad de líneas que desee que tenga su archivo de texto: "))

    if (i>0):

        for j in range(1,i+1,1):
            word = input(f"Digite la que cadena que desea guardar en la línea : ")
            archivo_texto.write(word+ '\n') 
    else:
        print("la cantidad de líneas debe ser mayor que cero")

    archivo_texto.close()

#MÉTODO PARA ESCRIBIR LÍNEAS DE TEXTO EN N CADENAS DIFERENTES (TESTADO)
def EscribirLineasDeTextoTest():
    correcto = False
    while (not correcto):
        try:
            EscribirLineasDeTexto()
            correcto = True
        except ValueError:
            print("la cantidad ingresada debe ser de tipo numérica")


# MÉTODO PARA MOSTRAR EL ARCHIVO
def MostrarArchivo():
    archivo = open('archivo_texto.txt','r')

    lista = archivo.readlines()
    j = 1
    for i in lista:
        print(f"la información que hay en la línea {j} es: {i}")
        j=j+1

# MÉTODO PARA MOSTRAR EL ARCHIVO (testeado)

def MostrarArchivoTest():
    correcto = False
    while not correcto:
        try:
            MostrarArchivo()
            correcto = True

            
        except FileNotFoundError as identifier:
            print("el arhivo está vacío")
            correcto = True




def Menu ():
    correcto = False
    while not correcto:
        try:
            op = 0
   
            salir = False
            while(not salir):
                print("----MENÚ PRINCIPAL")
                print("1.Guardar n candenas en n líneas de texto \n 2.Ver información del arhivo de texto \n 3.Salir")
                op = 0
                op = int(input("Elige una opción: "))
                
                if (op==1):
                    EscribirLineasDeTextoTest()
                
                elif (op==2):
                    MostrarArchivoTest()
                elif (op==3):
                    print("Suerte :) ")
                    salir = True
                elif ((op != 1) and (op!= 2) and (op !=3)):
                    print("ERROR, OPCIÓN INCORRECTA")
            correcto = True
        except:
            print("ERROR!,LA OPCIÓN ES DE TIPO NUMÉRICA")

Menu()



            



            

