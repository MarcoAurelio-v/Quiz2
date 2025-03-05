from Personas import Persona, Ingeniero, Arquitecto, Obrero

def primo(horas_trabajadas):
    is_primo = True
    n = horas_trabajadas-1 
    while n > 0:
        n_primo = horas_trabajadas % n
        if n_primo != 0:
            is_primo = False
        else:
            n -= 1

    return is_primo
    
def deficiente(horas_trabajadas):
    is_deficiente = True
    divs = 0
    n = horas_trabajadas-1
    
    while n > 0:
      if horas_trabajadas % n != 0:
          divs += n
    
    n_deficiente = horas_trabajadas-divs
    
    if n_deficiente > 0:
        is_deficiente = False
        
    return is_deficiente

def main():
    trabajadores_objetos = []
    trabajadores = []
 
    
    while True:
        ings = 0
        arq = 0
        menu = input("¡Bienvenido a Saman Constructions! \n Seleccione: \n\t 1. Añadir un trabajador de la obra \n\t 2. Ver trabajadores de la obra \n\t 3. Monto total pagado a los empleados \n\t 4. Cantidad de empleados por tipo \n\t 5. Promedio de pago para cada tipo de empleado \n---> ")
        if menu == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            cedula = int(input("Ingrese la cedula: "))
            horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
            for trabajador in trabajadores:
                trabajadores_objetos.append(Persona(nombre, apellido, cedula, horas_trabajadas))
                          
            tipo = input("Profesion: \n\t 1. Ingeniero \n\t 2. Arquitecto \n\t 3. Obrero \n\t---> ")
            if tipo == "1":
                ings = +1
                especialidad = input("Especialidad: \n\t 1. Ingeniero Civil \n\t 2. Ingeniero Electrico \n\t---> ")
                if especialidad == "1":
                    datos_especialidad = "Civil"
                elif especialidad == "2":
                    datos_especialidad = "Electrico"
                
            
                monto_factura = horas_trabajadas*25
        
            elif tipo == "2":
                especialidad = input("Especialidad: \n\t 1. Arquitecto Exterior \n\t 2. Arquitecto Interior \n\t---> ")
                if especialidad == "1":
                    datos_especialidad = "Exterior"
                elif especialidad == "2":
                    datos_especialidad = "Interior"
                    
                monto_factura = horas_trabajadas*10
                
            elif tipo == "3":
                especialidad = input("Especialidad: \n\t 1. Capataz \n\t 2. Obrero Novato \n\t---> ")
                if especialidad == "1":
                    datos_especialidad = "Capataz"
                elif especialidad == "2":
                    datos_especialidad = "Novato"
                    
                monto_factura = horas_trabajadas*5
                
            primo(horas_trabajadas)
            if primo(horas_trabajadas) == True:
                monto_factura = monto_factura/0.05
            deficiente(horas_trabajadas)
            if deficiente(horas_trabajadas) == True:
                monto_factura = monto_factura/0.10
                         
                    
            trabajadores_objetos.append(Persona(tipo, especialidad, monto_factura"$"))
            
        elif menu == "2":
            print(trabajadores_objetos)
            
        elif menu == "3":
            monto_total = 0
            for trabajador in trabajadores_objetos:
                monto_total+= monto_factura
        
        elif menu == "4":
            for trabajador in trabajadores_objetos:
                if tipo == 
                    
        else:
            print("Ingreso no valido")
        
        
        
        
            
main()
    