import string


class usuario:
    nombre: string
    contraseña: string
    usuario: string
    email: string
    premium: bool
    perfil:perfil

    def __init__(self, nombre:string, contraseña:string, usuario:string, email:string, premium:bool, perfil:perfil):

        def CrearUsuario():str