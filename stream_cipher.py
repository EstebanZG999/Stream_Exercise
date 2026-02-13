import random

def generar_keystream(seed: str, longitud: int) -> bytes:
    prng = random.Random(seed)

    ks = bytes(prng.randrange(0, 256) for _ in range(longitud))

    return ks