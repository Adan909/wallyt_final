from dao.dao_saldo import SaldoDAO
from dao.dao_usuario import UsuarioDAO
import pwinput

usuarios = UsuarioDAO()
saldos = SaldoDAO()

# Inicio de sesión
usuario = input("Usuario: ")
contraseña = pwinput.pwinput(prompt="Contraseña: ", mask='*')

if usuarios.verificar_usuario(usuario, contraseña):
    print("¡Inicio de sesión exitoso!")

    while True:
        print("\n1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Actualizar saldo manualmente")
        print("4. Ver saldo actual")
        print("5. Ver transacciones")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            try:
                monto = float(input("Monto a ingresar: $ "))
                nuevo_saldo = saldos.ingresar(usuario, monto)
                print(f"Nuevo saldo: ${nuevo_saldo:.2f}")
            except ValueError:
                print("Monto inválido.")
        elif opcion == "2":
            try:
                monto = float(input("Monto a retirar: $ "))
                nuevo_saldo = saldos.retirar(usuario, monto)
                if nuevo_saldo is not None:
                    print(f"Nuevo saldo: ${nuevo_saldo:.2f}")
                else:
                    print("Fondos insuficientes.")
            except ValueError:
                print("Monto inválido.")
        elif opcion == "3":
            saldos.actualizar_saldo_interactivo(usuario)