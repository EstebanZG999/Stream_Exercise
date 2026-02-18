from stream_cipher import cifrar


def ejemplo_2_1() -> None:
    mensaje = "HOLA SOY JUAN P, EL CISO"

    clave_a = "clave_A"

    clave_b = "clave_B"

    cifrado_a = cifrar(mensaje, clave_a)

    cifrado_b = cifrar(mensaje, clave_b)

    print("Ejemplo 2.1")
    print(f"Mensaje: {mensaje}")
    print(f"Cifrado con {clave_a}: {cifrado_a}")
    print(f"Cifrado con {clave_b}: {cifrado_b}")
    print(f"Son iguales? {cifrado_a == cifrado_b}")


if __name__ == "__main__":
    ejemplo_2_1()
