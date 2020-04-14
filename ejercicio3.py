import csv
import numpy as np
import pandas
# class Contacto:

#     def __init__(self,nombre,telefono,email):
#         self.nombre = nombre
#         self.telefono = telefono
#         self.email = email
#         print("Se ha creado un contacto nuevo con el nombre de :",self.nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre,self.telefono,self.email)


# class ListaContacto:
#     contactos =[]

#     def __init__(self):
#         listaDeContactos = open("archivo.csv",'a')
        
        
#         listaDeContactos.close()
#         del(listaDeContactos)

#     def agregarContactos(self,c):
#         self.contactos.append(c)
#         self.guardarContactosEnFicheroExterno()
    
#     def MostrarContactos(self):
#         for i in self.contactos:
#             print(i)

#     def guardarContactosEnFicheroExterno(self):
#         with open("archivo.csv",'w',newline='') as file:
#             writer = csv.writer(file,delimiter=',')
#             writer.writerow(self.contactos)
        

#     def mostrarInforFicheroExterno(self):
#         print("la información del fichero externo es la siguiente: ")
#         with open('archivo.csv','r') as csv_file:
#             csv_reader = csv.reader(csv_file)
#             for row in csv_reader:
#                 print(row)



# milista = ListaContacto()

# c3 = Contacto("Pablo","45234234","jufiahf@mai-fefopcm")

# milista.agregarContactos(c3)
# milista.mostrarInforFicheroExterno()


     
    
    

    


def Escribir():
    correcto = False
    while not correcto:
        try:    
            oneContact = []
            print("Para agregar un nuevo contacto, diligencia los siguientes campos: ")
            name = input("Digite el nombre de su contacto: ")
            phone = int(input("Digite el número de su contacto: "))
            email = input("Digite el email de su contacto: ")

        
            oneContact=[name,phone,email]
        
            with open('contactos.csv','a',newline='') as file:
                writer = csv.writer(file,delimiter=",")
                writer.writerow(oneContact)
                print("-----------------CONTACTO GUARDADO CORRECTAMENTE--------------------")
                print("\n")
            correcto = True
        except ValueError:
            print("ERROR, RECUERDE QUE LA CANTIDAD INGRESADA EN EL CAMPO DEL TELÉFONO, DEBE SER \n DE TIPO NUMÉRICA")
                


def Leer():
    
    with open('contactos.csv','r') as file:
        print("-----------------LISTA DE CONTACTOS--------------------")
        print("[Nombre , Telefono, Email]")
        file_reader = csv.reader(file)
        for row in file_reader:
            print(row)
    
       

def LeerTodo():
    correcto = False
    while not correcto:
        try:
            Leer()
            correcto = True

            
        except FileNotFoundError as identifier:
            print("el arhivo está vacío")
            correcto = True
            
    
       



def Menu():
    correcto = False
    while not correcto:
        try:
            op = 0
   
            salir = False
            while(not salir):
                print("-----------------GESTION DE AGENDA--------------------")
                print("----MENÚ PRINCIPAL")
                print("1.Agregar Contactos \n 2.Ver Contactos \n 3.Salir")
                op = 0
                op = int(input("Elige una opción: "))
                
                if (op==1):
                    Escribir()
                
                elif (op==2):
                    LeerTodo()
                elif (op==3):
                    print("Suerte :) ")
                    salir = True
                elif ((op != 1) and (op!= 2) and (op !=3)):
                    print("ERROR, OPCIÓN INCORRECTA")
            correcto = True
        except:
            print("ERROR!,LA OPCIÓN ES DE TIPO NUMÉRICA")
     
        
        
Menu()
        
        
        
         


