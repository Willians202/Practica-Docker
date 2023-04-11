import configuration as C
import consultas as con
import logging
import database as db
import os

# setting up the logging
logging.Logger(name="Logs")
logging.basicConfig(filename=C.LOG_FILE, level=logging.DEBUG, format="%(asctime)s %(message)s")

# log a message indicating the start of the application
logging.info("Starting ...")

opcion = None
while opcion != 6:
    os.system("cls")
    print("Seleccione una opción:")
    print("1. Consulta 1")
    print("2. Consulta 2")
    print("3. Consulta 3")
    print("4. Consulta 4")
    print("5. Consulta 5")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    try:
        opcion = int(opcion)
    except ValueError:
        print("ERROR: Ingrese un número válido.")
        continue
        
    if opcion == 1:
        print("Ha seleccionado la Opción 1.")
        try:
            logging.info("Ejecutando la consulta 1")
            result = con.Con1()
        except:
            logging.error("La consulta 1 falló")
            result = "La consulta 1 falló"
        print(result)        
        input("Presione Enter para continuar...")
    elif opcion == 2:
        print("Ha seleccionado la Opción 2.")
        try:
            logging.info("Ejecutando la consulta 2")
            result = con.Con2()
        except:
            logging.error("La consulta 2 falló")
            result = "La consulta 2 falló"
        print(result)
        input("Presione Enter para continuar...")
    elif opcion == 3:
        print("Ha seleccionado la Opción 3.")
        try:
            logging.info("Ejecutando la consulta 3")
            result = con.Con3()
        except:
            logging.error("La consulta 3 falló")
            result = "La consulta 3 falló"
        print(result)
        input("Presione Enter para continuar...")
    elif opcion == 4:
        print("Ha seleccionado la Opción 4.")
        try:
            logging.info("Ejecutando la consulta 4")
            result = con.Con4()
        except:
            logging.error("La consulta 4 falló")
            result = "La consulta 4 falló"
        print(result)
        input("Presione Enter para continuar...")
    elif opcion == 5:
        print("Ha seleccionado la Opción 5.")
        try:
            logging.info("Ejecutando la consulta 5")
            result = con.Con5()
        except:
            logging.error("La consulta 5 falló")
            result = "La consulta 5 falló"
        print(result)
        input("Presione Enter para continuar...")
    elif opcion == 6:
        print("Saliendo...")
        logging.info("Ending ...")
        break
    else:
        print("ERROR: Seleccione una opción válida.")
        continue



