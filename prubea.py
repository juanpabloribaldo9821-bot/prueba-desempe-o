import csv
import os 

ARCHIVO = 'users.csv'
CAMPOS = ['id', 'name', 'course' '']
def initialize_file():

    
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()

def create_record(datos):

    initialize_file()
    with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow(datos)

def read_log():
    
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def update_record (id_buscado, nuevos_datos):
    
    filas = read_log()
    actualizado = False
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        for fila in filas:
            if fila['id'] == str(id_buscado):
                writer.writerow(nuevos_datos)
                actualizado = True
            else:
                writer.writerow(fila)
    return actualizado

def delete_record(id_buscado):
   
    filas = read_log()
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        for fila in filas:
            if fila['id'] != str(id_buscado):
                writer.writerow(fila)


create_record({'id': '1', 'name': 'Ribaldo', 'course': 'PYTHON'})
create_record({'id': '2', 'name': 'Luis', 'course':  'JAVA'})

print("Registros actuales:", read_log())

update_record('1', {'id': '1', 'name': 'Ribaldo', 'course': 'PYTHON'})
delete_record('2')

print("final registration:", read_log())

def create_arrangement():
    lista = []
    continuar_llenando = True
    
    print("\n--- putting together the arrangement ---")
    while continuar_llenando:
        dato = input(" enter an element(or type ready to finish): ")
        
        if dato.lower() == 'listo':
            continuar_llenando = False 
        else:
           
            lista.append(dato) 
            
    return lista

def search_items(lista):
    if not lista:
        print("the array is empty.")
        return

    print("\n--- seeker ---")
    busqueda = input("¿What do you want to search for??: ")
    
    if busqueda in lista:
        print(f"'{busqueda}' if it's in the arrangement.")
    else:
        print(f"'{busqueda}' not found.")



mi_lista = []
running_program = True 

while running_program:
    print("\n--- Main menu ---")
    print("1. create / add elements")
    print("2. search for an element")
    print("3. see the whole arrangement")
    print("4. exit")
    
    opcion = input("choose an option (1-4): ")

    if opcion == "1":
        new_information = create_arrangement()
        mi_lista.extend(new_information) 
        print("¡updated list!")

    elif opcion == "2":
        search_items(mi_lista)

    elif opcion == "3":
        print(f"\nyour current arrangement is: {mi_lista}")

    elif opcion == "4":
        print("leaving the program..")
       
        running_program= False 

    else:
        print("Invalid option, please try again.")