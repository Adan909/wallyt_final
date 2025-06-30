from dao.dao_saldo import SaldoDAO  # Importa la clase SaldoDAO desde el módulo dao_saldo
from dao.dao_usuario import UsuarioDAO  # Importa la clase UsuarioDAO desde el módulo dao_usuario
import pwinput  # Biblioteca para entrada de contraseñas con máscara

# Instancia de las clases DAO para manejar usuarios y saldos
usuarios = UsuarioDAO()
saldos = SaldoDAO()

# Definición de la función menu
def menu():
    while True:
        # Menú principal con opciones
        print("\n1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Actualizar saldo manualmente")
        print("4. Ver saldo actual")
        print("5. Ver transacciones")
        print("6. Salir")

        # Solicita al usuario que seleccione una opción
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Opción para ingresar dinero
            try:
                monto = float(input("Monto a ingresar: $ "))  # Solicita el monto a ingresar
                nuevo_saldo = saldos.ingresar(usuario, monto)  # Llama al método para ingresar dinero
                print(f"Nuevo saldo: ${nuevo_saldo:.2f}")  # Muestra el nuevo saldo
            except ValueError:  # Manejo de errores si el monto no es válido
                print("Monto inválido.")
        elif opcion == "2":  # Opción para retirar dinero
            try:
                monto = float(input("Monto a retirar: $ "))  # Solicita el monto a retirar
                nuevo_saldo = saldos.retirar(usuario, monto)  # Llama al método para retirar dinero
                if nuevo_saldo is not None:  # Verifica si la operación fue exitosa
                    print(f"Nuevo saldo: ${nuevo_saldo:.2f}")  # Muestra el nuevo saldo
                else:
                    print("Fondos insuficientes.")  # Mensaje si no hay fondos suficientes
            except ValueError:  # Manejo de errores si el monto no es válido
                print("Monto inválido.")
        elif opcion == "3":  # Opción para actualizar el saldo manualmente
            saldos.actualizar_saldo_interactivo(usuario)  # Llama al método para actualizar el saldo
        elif opcion == "4":  # Opción para ver el saldo actual
            actual = saldos.obtener_saldo(usuario)  # Obtiene el saldo actual
            print(f"Tu saldo actual es: ${actual:.2f}")  # Muestra el saldo actual
        elif opcion == "5":  # Opción para ver las transacciones
            saldos.ver_transacciones(usuario)  # Llama al método para ver las transacciones
        elif opcion == "6":  # Opción para salir del sistema
            print("Saliendo del sistema...")  # Mensaje de salida
            break  # Rompe el bucle para salir
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje para opciones inválidas


# Bucle principal para el inicio de sesión
while True:
    usuario = input("Usuario: ")  # Solicita el nombre de usuario
    contraseña = pwinput.pwinput(prompt="Contraseña: ", mask='*')  # Solicita la contraseña con máscara

    if usuarios.verificar_usuario(usuario, contraseña):  # Verifica las credenciales del usuario
        print("¡Inicio de sesión exitoso!")  # Mensaje de éxito
        menu()  # Llama al menú principal
        break  # Rompe el bucle después de un inicio de sesión exitoso
    else:
        print("Usuario o contraseña incorrecta. Intenta de nuevo.")  # Mensaje de error para credenciales incorrectas
