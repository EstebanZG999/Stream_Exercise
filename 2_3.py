from stream_cipher import generar_keystream


def ejemplo_2_3() -> None:
    mensaje = "Mensaje de prueba para longitud"
    
    mensaje_bytes = mensaje.encode("utf-8")

    clave = "clave_longitud"

    keystream_igual = generar_keystream(clave, len(mensaje_bytes))

    keystream_largo = generar_keystream(clave, len(mensaje_bytes) + 10)

    keystream_corto = generar_keystream(clave, 8)

    cifrado_igual = bytes(m ^ k for m, k in zip(mensaje_bytes, keystream_igual))

    cifrado_largo = bytes(m ^ k for m, k in zip(mensaje_bytes, keystream_largo))

    print("Ejemplo 2.3")
    print(f"Longitud mensaje: {len(mensaje_bytes)}")
    print(f"Longitud keystream igual: {len(keystream_igual)}")
    print(f"Longitud keystream largo: {len(keystream_largo)}")
    print(f"Longitud keystream corto: {len(keystream_corto)}")
    print("Resultado igual vs largo:", cifrado_igual == cifrado_largo)

if __name__ == "__main__":
    ejemplo_2_3()
