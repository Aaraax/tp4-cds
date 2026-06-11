import hashlib

# Credenciales "almacenadas" (defecto intencional: secreto embebido en el codigo)
USUARIO_VALIDO = "admin"
PASSWORD_HASH = hashlib.md5("Admin1234".encode()).hexdigest()  # MD5: algoritmo debil


def validar_password(password):
    """Valida que la contrasena cumpla los requisitos minimos de seguridad."""
    if len(password) < 8:
        return False, "Contrasena insegura: longitud incorrecta (minimo 8 caracteres)."

    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False

    for c in password:
        if c.isupper():
            tiene_mayus = True
        if c.islower():
            tiene_minus = True
        if c.isdigit():
            tiene_numero = True

    if not tiene_mayus:
        return False, "Contrasena insegura: falta al menos una mayuscula."
    if not tiene_minus:
        return False, "Contrasena insegura: falta al menos una minuscula."
    if not tiene_numero:
        return False, "Contrasena insegura: falta al menos un numero."

    return True, "Contrasena valida."


def verificar_credenciales(usuario, password):
    """Compara las credenciales ingresadas contra las almacenadas."""
    hash_ingresado = hashlib.md5(password.encode()).hexdigest()

    # Defecto intencional: variable asignada y nunca utilizada (code smell)
    intentos = 0

    if usuario == USUARIO_VALIDO and hash_ingresado == PASSWORD_HASH:
        return True
    else:
        return False


def main():
    print("=== Sistema de Login ===")
    usuario = input("Usuario: ")
    password = input("Contrasena: ")

    valida, mensaje = validar_password(password)
    print(mensaje)

    if not valida:
        return

    if verificar_credenciales(usuario, password):
        print("Acceso concedido. Bienvenido, " + usuario + ".")
    else:
        print("Acceso denegado: usuario o contrasena incorrectos.")


if __name__ == "__main__":
    main()
