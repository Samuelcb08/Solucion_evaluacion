usuarios = []
bicicletas_disponibles = ["rosada", "Azul", "Roja", "Amarillo","Verde"]
bicicletas_prestadas = {}

def registrar_usuario():
    print("Registro de nuevo usuario:")
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    nombre_completo = input("Nombre completo: ")
    tarjeta = input("Número de tarjeta: ")
    Correo= input("Correo: ")

    # Verificar si el nombre de usuario ya existe
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Este nombre de usuario ya está en uso. Por favor, elige otro.")
            return

    usuarios.append({"nombre": nombre, "contraseña": contraseña, "nombre_completo": nombre_completo, "tarjeta": tarjeta ,"Correo":Correo})
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    print("Inicio de sesión:")
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            print("Inicio de sesión exitoso. ¡Bienvenido a la pagina BicicletasPower".format(usuario["nombre"]))
            prestar_bicicleta(usuario["nombre"])
            return

    print("Nombre de usuario o contraseña incorrectos.")

def prestar_bicicleta(nombre_usuario):
    if nombre_usuario not in bicicletas_prestadas:
        print("\nBicicletas disponibles en este momento:")
        for i, bicicleta in enumerate(bicicletas_disponibles, 1):
            print("{}. {}".format(i, bicicleta))

        opcion = input("Selecciona una bicicleta para prestar (1-{}): ".format(len(bicicletas_disponibles)))

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(bicicletas_disponibles):
                bicicleta_prestada = bicicletas_disponibles.pop(opcion - 1)
                origen = input("Origen del viaje: ")
                destino = input("Destino del viaje: ")

                bicicletas_prestadas[nombre_usuario] = {
                    "bicicleta": bicicleta_prestada,
                    "origen": origen,
                    "destino": destino
                }
                print("Bicicleta {} prestada con éxito a {} para el viaje desde {} hasta {}.".format(
                    bicicleta_prestada, nombre_usuario, origen, destino))
            else:
                print("Opción no válida. Por favor, selecciona un número válido.")
        except ValueError:
            print("Opción no válida. Por favor, selecciona un número válido.")
    else:
        print("Ya tienes una bicicleta prestada. No puedes prestar otra hasta que la devuelvas.")

while True:
    print("\nOpciones:")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
