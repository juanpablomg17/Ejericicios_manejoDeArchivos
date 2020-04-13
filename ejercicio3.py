import csv





def Escribir():
    contacts = []
    oneContact = []
    n = int(input("cuantos contactos desea agregar: "))
    
    for i in range(0,n,1):
        name = input("Digite el nombre de su contacto: ")
        phone = int(input("Digite el número de su contacto: "))
        email = input("Digite el email de su contacto: ")

        print("Ingrese la información de otro contacto...")
        oneContact=[name,phone,email]
        contacts.append(oneContact)

    with open("contactos.csv",'w',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        
        writer.writerow(["Nombre","Telefono","Email"])
        
        writer.writerows(contacts)
        

    


        



    # archivo_contactos = open("contactos.csv","w")
    # archivo_contactos_w = csv.writer(archivo_contactos,delimiter="-")

    # cabecera = ["Nombre","Telefono","Email"]
    # archivo_contactos_w.writerow(cabecera)
    # op = input("Desea Agregar un nuevo contacto?  y/n")
    
    # if ((op == 'y') or op == 'Y'):
    #     n = int(input("¿cuántos contactos desea agregar?"))
    #     new_contactos= []
    #     for i in range(1,n+1,1):
    #         name = input("Digite el nombre de su contacto: ")
    #         phone = int(input("Digite el número de su contacto: "))
    #         email = input("Digite el email de su contacto: ")
    #         one_contact=[name,phone,email]

    #         new_contactos.append(one_contact)
    #         archivo_contactos_w.writerows(new_contactos)
    # else: 
    #     print("entonces para qué mierda le da a esta opción")

        
    
    

    # archivo_contactos.close()
    # del (archivo_contactos)

def Leer():
    with open('contactos.csv','r') as csv_file:

        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            print(row)


Leer()


