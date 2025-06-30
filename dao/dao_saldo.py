class SaldoDAO:
    def __init__(self):
        # Inicializa los saldos de los usuarios y sus transacciones
        self.saldos = {
            "admin": 1000.0,  # Saldo inicial del usuario "admin"
            "duran": 750.0    # Saldo inicial del usuario "duran"
        }
        self.transacciones = {
            "admin": [],  # Lista de transacciones del usuario "admin"
            "duran": []   # Lista de transacciones del usuario "duran"
        }

    def obtener_saldo(self, usuario):
        # Devuelve el saldo del usuario especificado, o None si no existe
        return self.saldos.get(usuario, None)

    def ingresar(self, usuario, monto):
        # Agrega un monto al saldo del usuario si existe
        if usuario in self.saldos:
            self.saldos[usuario] += monto  # Incrementa el saldo
            # Registra la transacción en el historial
            self.transacciones[usuario].append(f"Ingreso: +${monto:.2f}")
            return self.saldos[usuario]  # Devuelve el saldo actualizado
        return None  # Devuelve None si el usuario no existe

    def retirar(self, usuario, monto):
        # Resta un monto del saldo del usuario si existe y tiene suficiente saldo
        if usuario in self.saldos and self.saldos[usuario] >= monto:
            self.saldos[usuario] -= monto  # Decrementa el saldo
            # Registra la transacción en el historial
            self.transacciones[usuario].append(f"Retiro: -${monto:.2f}")
            return self.saldos[usuario]  # Devuelve el saldo actualizado
        return None  # Devuelve None si el usuario no existe o no tiene suficiente saldo

    def actualizar_saldo_interactivo(self, usuario):
        # Permite actualizar el saldo de un usuario de forma interactiva
        saldo_actual = self.obtener_saldo(usuario)  # Obtiene el saldo actual
        if saldo_actual is None:
            print("Usuario sin cuenta.")  # Mensaje si el usuario no existe
            return

        while True:
            try:
                # Solicita al usuario ingresar una cantidad para agregar o restar
                cantidad = input("Ingresa la cantidad a agregar o restar (usa '-' para restar): $ ")
                cantidad = float(cantidad)  # Convierte la entrada a un número flotante
                saldo_actual += cantidad  # Actualiza el saldo
                self.saldos[usuario] = saldo_actual  # Guarda el saldo actualizado
                # Registra la transacción en el historial
                self.transacciones[usuario].append(
                    f"Actualización manual: {'+' if cantidad >= 0 else ''}${cantidad:.2f}"
                )
                print(f"Saldo actualizado: ${saldo_actual:.2f}")  # Muestra el saldo actualizado
                return saldo_actual  # Devuelve el saldo actualizado
            except ValueError:
                # Maneja errores si el usuario ingresa un valor no numérico
                print("Por favor, ingresa un valor numérico válido.")

    def ver_transacciones(self, usuario):
        # Muestra el historial de transacciones de un usuario
        if usuario not in self.transacciones or not self.transacciones[usuario]:
            print("No hay transacciones registradas.")  # Mensaje si no hay transacciones
            return
        print("Historial de transacciones:")  # Encabezado del historial
        for t in self.transacciones[usuario]:
            print(f" - {t}")  # Imprime cada transacción
