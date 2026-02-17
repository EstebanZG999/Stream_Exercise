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


mensaje_original = "Hola mundo"
clave = "mi_clave"

c = cifrar(mensaje_original, clave)
d = descifrar(c, clave)

print(d == mensaje_original)
