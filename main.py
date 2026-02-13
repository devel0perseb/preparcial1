usuarios = [
    {"nombre": "Ana", "correo": "ana@bancolombia.com", "password": "123", "empresa": "Bancolombia", "rol": "Gestor"},
    {"nombre": "Luis", "correo": "luis@epm.com", "password": "123", "empresa": "EPM", "rol": "Gestor"},
    {"nombre": "Marta", "correo": "marta@nutresa.com", "password": "123", "empresa": "Grupo Nutresa", "rol": "Gestor"},
    {"nombre": "Juan", "correo": "juan@postobon.com", "password": "123", "empresa": "Postobón", "rol": "Gestor"},
    {"nombre": "Sofia", "correo": "sofia@bancolombia.com", "password": "123", "empresa": "Bancolombia", "rol": "Gestor"}
]

intentos = 3
acceso = False

while intentos > 0:
    correo = input("Correo: ")
    password = input("Password: ")

    for u in usuarios:
        if u["correo"] == correo and u["password"] == password:
            print("Bienvenido", u["nombre"])
            acceso = True
            break

    if acceso:
        break
    else:
        intentos -= 1
        print("Datos incorrectos. Intentos restantes:", intentos)

if acceso:

    recolecciones = {
        "PET": [],
        "CARTON": [],
        "VIDRIO": [],
        "METAL": []
    }

    for material in recolecciones:
        print("\nMaterial:", material)
        for i in range(20):
            kg = float(input("Ingrese kg: "))
            recolecciones[material].append(kg)

    total_global = 0
    cantidad_total = 0

    print("\n--- REPORTE ---")

    for material in recolecciones:
        promedio = sum(recolecciones[material]) / len(recolecciones[material])
        total_global += sum(recolecciones[material])
        cantidad_total += len(recolecciones[material])

        if promedio < 8:
            clasificacion = "Bajo"
        elif promedio <= 15:
            clasificacion = "Estable"
        else:
            clasificacion = "Alto"

        print(material, "- Promedio:", round(promedio,2), "- Clasificación:", clasificacion)

    promedio_global = total_global / cantidad_total

    if promedio_global < 10:
        clas_global = "Alerta"
    elif promedio_global < 15:
        clas_global = "Operación normal"
    else:
        clas_global = "Jornada sobresaliente"

    print("\nPromedio Global:", round(promedio_global,2))
    print("Clasificación Global:", clas_global)

else:
    print("Acceso bloqueado.")