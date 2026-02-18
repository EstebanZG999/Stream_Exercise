from stream_cipher import cifrar


def ejemplo_2_2() -> None:
    mensaje_1 = "ESTA VEZ NO SOY JUAN P"

    mensaje_2 = "PORQUE JUAN P ES BATMAN"

    clave = "clave_igual"

    cifrado_1 = cifrar(mensaje_1, clave)

    cifrado_2 = cifrar(mensaje_2, clave)

    xor_cifrados = bytes(a ^ b for a, b in zip(cifrado_1, cifrado_2))

    xor_planos = bytes(a ^ b for a, b in zip(mensaje_1.encode("utf-8"), mensaje_2.encode("utf-8")))

    print("Ejemplo 2.2")
    print(f"Mensaje 1: {mensaje_1}")
    print(f"Mensaje 2: {mensaje_2}")
    print(f"C1 xor C2 == P1 xor P2 ? {xor_cifrados == xor_planos}")
    print(f"C1 xor C2: {xor_cifrados}")


if __name__ == "__main__":
    ejemplo_2_2()
