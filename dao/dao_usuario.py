import hashlib

class UsuarioDAO:
    # Constructor de la clase UsuarioDAO
    def __init__(self):
        # Diccionario que almacena usuarios y contraseñas cifradas
        self.usuarios = {
            "admin": self.cifrar_contraseña("admin123"),  # Usuario "admin" con contraseña cifrada
            "duran": self.cifrar_contraseña("duran456")  # Usuario "duran" con contraseña cifrada
        }

    # Método para cifrar una contraseña utilizando el algoritmo SHA-256
    def cifrar_contraseña(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()

    # Método para verificar si un usuario y contraseña son válidos
    def verificar_usuario(self, usuario, contraseña):
        if usuario in self.usuarios:  # Verifica si el usuario existe en el diccionario
            # Compara la contraseña cifrada proporcionada con la almacenada
            return self.usuarios[usuario] == self.cifrar_contraseña(contraseña)
        return False  # Retorna False si el usuario no existe

    # Método para verificar si un usuario existe en el diccionario
    def existe_usuario(self, usuario):
        return usuario in self.usuarios
