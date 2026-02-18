# Prompt para IA: Generame unas pruebas unitarias para esta siguiente implementación de codigo stream cipher (le paso el codigo que hice)


from stream_cipher import cifrar, descifrar

def test_descifrado_correcto():
    mensaje = "Prueba de cifrado"
    clave = "clave_test"
    c = cifrar(mensaje, clave)
    d = descifrar(c, clave)
    assert d == mensaje

def test_claves_diferentes():
    mensaje = "Mismo mensaje"
    c1 = cifrar(mensaje, "clave1")
    c2 = cifrar(mensaje, "clave2")
    assert c1 != c2

def test_determinismo():
    mensaje = "Mensaje deterministico"
    clave = "misma_clave"
    c1 = cifrar(mensaje, clave)
    c2 = cifrar(mensaje, clave)
    assert c1 == c2

def test_diferentes_longitudes():
    clave = "clave_longitud"
    mensajes = [
        "a",
        "mensaje corto",
        "mensaje un poco mas largo para probar"
    ]
    for m in mensajes:
        c = cifrar(m, clave)
        d = descifrar(c, clave)
        assert d == m

if __name__ == "__main__":
    test_descifrado_correcto()
    test_claves_diferentes()
    test_determinismo()
    test_diferentes_longitudes()
    print("Todas las pruebas pasaron correctamente.")
