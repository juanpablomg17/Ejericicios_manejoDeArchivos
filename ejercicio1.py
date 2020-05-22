from io import open

def EscribirArchivo():
    archivo_texto = open("ejercicio1.txt","a")
    word = input("Digite la que cadena que desea guardar en el archivo: ")
    archivo_texto.write(word+ '\n') 
    print("\n ¡CADENA DE TEXTO GUARDADA CORRECTAMENTE!")

def MostrarBytes():

    arhivo2 = open('ejercicio1.txt','r')

    n = int(input("Digite la cantidad de bytes que desea imprimir: "))

    cantidad_bytes = arhivo2.read(n)
    print("------------------------------------------------------------------")
    print(f"los {n} primeros bytes corresponden a la cadena: {cantidad_bytes}")
    print("-------------------------------------------------------------------")
    arhivo2.seek(0)

   

def MostrarBytesTest():

    correcto = False
    while (not correcto):
        try:
            MostrarBytes()
            correcto = True

        except FileNotFoundError as identifier:
            print("-------------------------------------")
            print("ERROR!!!,El archivo está vacío")
            print("-------------------------------------")
            correcto = True


def Menu():
    correcto = False
    while not correcto:
        try:
            op = 0
   
            salir = False
            while(not salir):
                print("------------------MENÚ PRINCIPAL-----------------------")
                print(" 1.Escribir en archivo \n 2.Ver n primeros bytes del archivo \n 3.Salir")
                op = 0
                op = int(input("Elige una opción: "))
                
                if (op==1):
                    EscribirArchivo()
                
                elif (op==2):
                    MostrarBytesTest()
                elif (op==3):
                    print("Suerte :) ")
                    salir = True
                elif ((op != 1) and (op!= 2) and (op !=3)):
                    print("ERROR, OPCIÓN INCORRECTA")
            correcto = True
        except:
            print("ERROR!,LA OPCIÓN ES DE TIPO NUMÉRICA")
    

    
Menu()
    