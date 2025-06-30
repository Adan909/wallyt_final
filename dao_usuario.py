class UsuarioDAO:
    def __init__(self):
        self.usuarios = {
            "admin": self.cifrar_contraseña("admin123"),
            "duran": self.cifrar_contraseña("duran456")
        }

    def verificar_usuario(self, usuario, contraseña):
        if usuario in self.usuarios:
            return self.usuarios[usuario] == self.cifrar_contraseña(contraseña)
        return False

    def existe_usuario(self, usuario):
        return usuario in self.usuarios
