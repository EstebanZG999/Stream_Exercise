import random

def generar_keystream(seed: str, longitud: int) -> bytes:
    prng = random.Random(seed)

    ks = bytes(prng.randrange(0, 256) for _ in range(longitud))

    return ks

def cifrar(mensaje: str, clave: str) -> bytes:
    mensaje_bytes = mensaje.encode('utf-8')

    keystream = generar_keystream(clave, len(mensaje_bytes))

    cifrado = bytes(m ^ k for m, k in zip(mensaje_bytes, keystream))

    return cifrado

def descifrar(cifrado: bytes, clave: str) -> str:
    keystream = generar_keystream(clave, len(cifrado))

    mensaje_bytes = bytes(c ^ k for c, k in zip(cifrado, keystream))

    mensaje = mensaje_bytes.decode('utf-8')

    return mensaje


if __name__ == "__main__":

    mensaje_og = "Hola mundo"
    clave_og = "mi_clave"

    ci = cifrar(mensaje_og, clave_og)
    de = descifrar(ci, clave_og)

    print(de == mensaje_og)

    ejemplos = [
        ("Hola mundo", "mi_clave"),
        ("Hola soy Juan P CISO", "ciso1234"),
        ("La verdad que esto de cifrados esta interesante", "clave_del_pentagono")
    ]

    for mensaje_original, clave in ejemplos:
        c = cifrar(mensaje_original, clave)
        d = descifrar(c, clave)

        print("Texto:", mensaje_original)
        print("Clave:", clave)
        print("Cifrado:", c.hex())
        print("Descifrado:", d)
