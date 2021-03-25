import pandas as pd
materiales = {}
switchG = True
separador = ("*" * 50)

while switchG:
    print(separador)
    print("***MENÚ PRINCIPAL***")
    print("|1. Registro de una Venta|")
    print("|2. Consultar una Venta  |")
    print("|3. Salir                |")
    eleccion = int(input("¿Qué opción elegira? "))
    if eleccion == 1:
        switchA = True
        while switchA:
            key = int(input("Ingresa el Folio de venta: "))
            producto = input("Dame el nombre del Producto: ")
            descripcion = input("Dame su Descripcion: ")
            cantidad_piezas = float(input("Dame su Cantidad de Piezas a Vender: "))
            precio_venta = float(input("Dame su Precio Venta: "))
            monto_total = cantidad_piezas * precio_venta
            print(f"El monto total a pagar es de ${monto_total}")
            materiales[key] = [producto,descripcion,cantidad_piezas,precio_venta]
            print("***VENTA AGREGADA***")
            decision = int(input("¿Quiere seguir introduciendo productos? 1)Si 2)No "))
            if decision == 2:
                switchA = False
    elif eleccion == 2:
        materiales_ventas = pd.DataFrame(materiales)
        materiales_ventas.index = ["Producto","Descripcion","Cantidad Piezas Vendidas","Precio Unitario de Venta"]
        print(materiales_ventas)
            
    elif eleccion == 3:
        switchG = False
        print("*SALIDA DEL PROGRAMA*")
    else:
        print("Esta opción no es válida")