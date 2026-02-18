# Stream Cipher – Laboratorio de Cifrados de Información

## Descripción del Proyecto

Este proyecto implementa un esquema básico de cifrado de flujo (stream cipher) utilizando la operación XOR entre el mensaje en texto plano y un keystream pseudoaleatorio generado a partir de una clave (seed).

El objetivo del laboratorio es comprender el funcionamiento fundamental de los stream ciphers, analizar los riesgos asociados a la reutilización del keystream y evaluar las diferencias entre una implementación educativa y los algoritmos criptográficos modernos utilizados en entornos reales.

La implementación utiliza el módulo random de Python para generar un keystream determinístico basado en una clave proporcionada por el usuario. El cifrado y descifrado se realizan aplicando la operación XOR byte a byte.


## Estructura del Proyecto

stream_cipher.py → Implementación del keystream, cifrado y descifrado.

test_stream.py → Pruebas unitarias para validar el comportamiento del sistema.

README.md → Documentación del proyecto.

## Instrucciones de Instalación y Uso

### Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>


### Ejecutar el archivo principal:

python stream_cipher.py


### Ejecutar las pruebas unitarias:

python test_stream.py


Si todas las pruebas pasan correctamente, se mostrará el mensaje:

Todas las pruebas pasaron correctamente.


# Parte 2: Análisis de Seguridad

## 2.1 Variación de la Clave

### ¿Qué sucede cuando cambia la clave utilizada para generar el keystream? Demuestre con un ejemplo concreto.

Cuando se cambia la clave utilizada para generar el keystream, este keystream generado tambien cambia. La misma clave siempre va a genera el mismo keystream, asimismo si la clave cambia el keystream cambia tambien, produciento un texto cifrado diferente aunque el mensaje sea el mismo.

## 2.2 Reutilización del Keystream (5 puntos)

### ¿Qué riesgos de seguridad existen si reutiliza el mismo keystream para cifrar dos mensajes diferentes? Implemente un ejemplo que demuestre esta vulnerabilidad.

Si se reutiliza el mismo keystream para cifrar dos mensajes diferentes, puede ser que el atacante pueda eliminar el keystream y relacionar los dos mensajes. En terminos simples, si un atacante conoce parte de un mensaje, puede recuperar parte del otro tambien. 

Sugerencia: Cifre dos mensajes con la misma clave y analice qué información puede extraer un
atacante que intercepte ambos textos cifrados.

## 2.3 Longitud del Keystream (5 puntos)

### ¿Cómo afecta la longitud del keystream a la seguridad del cifrado? Considere tanto keystreams más cortos como más largos que el mensaje.

La longitud del keystream afecta a la seguridad del cifrado mediante siento keystream mas corto, keystream mas largo y keystream igual que el mensaje. Cuando el keystream es mas corto que el mensaje se tiene que repetir el keystream lo cual introduce periodicidad. Esto convierte al cifrado vulnerable a analisis estadisticos. Cuando el keystream es mas largo, eso no representa ningun riesgo a la seguridad ya que simplemente no se utilizan los bytes extras. Por ultimo, cuando el keystream es igual que el mensaje, el comportamiento es el esperado, cada byte del mensaje se cifra con cada byte unico del keystream. Asi que para que la seguridad no sea afectada el keystream tiene que ser al menos de la misma longitud del mensaje o mayor. 

## 2.4 Consideraciones Prácticas (5 puntos)

### ¿Qué consideraciones debe tener al generar un keystream en un entorno de producción real Mencione al menos 3 aspectos críticos.

1. No utilizar PRNG muy simples como el que generamos utilizando RANDOM
2. No utilizar el mismo keystream, que cada mensaje utilice un nonce para evitar la reutilizacion de flujo. 
3. Utilizar algoritmos modernos de cifrados que esten auditados y probados como el ChaCha20. 
4. Que el keystream sea del mismo largo o mayor al mensaje, para evitar que se repita la periodicidad.

# Parte 3

## 3.1 Ejemplos de Entrada/Salida

A continuación se muestran ejemplos reales utilizando la implementación desarrollada.

### Ejemplo 1

Texto plano:
Hola mundo

Clave utilizada:
mi_clave

Texto cifrado (hex):
aafded61de52617ca36c

Texto descifrado:
Hola mundo

### Ejemplo 2

Texto plano:
Hola soy Juan P CISO

Clave utilizada:
ciso1234

Texto cifrado (hex):
00d21b98db9ecabc0436db136a0814d97931f897

Texto descifrado:
Hola soy Juan P CISO

### Ejemplo 3

Texto plano:
La verdad que esto de cifrados esta interesante

Clave utilizada:
clave_del_pentagono

Texto cifrado (hex):
d5c5499024427c6da85428d81bd89a327e5132d8f71a3157cb7acabceb7689f9f5dc59c3c15991ac538ef96ec267f2

Texto descifrado:
La verdad que esto de cifrados esta interesante


# Parte 4: Reflexión Técnica

## 4.1 Limitaciones de PRNG simples

Los generadores simple pseudoaleatorios como random.Random() tienen un comportamiento determinista y por lo tanto no sirven para aplicaciones criptográficas ya que un atacante puede predecir las salidas, incluso si esto lo logra a partir de intentar inferir la seed o desde el estado interno siempre y cuando disponga de suficientes salidas del PRNG. Por ello, aunque estos generadores pueden mostrarse como buenos generadores para simulaciones no servirían para resistir ataques de atacante activos. Todo PRNG tiene un período finito, lo que quiere decir que se repiten todas las salidas inevitablemente. En criptografía no solo basta con que una salida "se vea aleatoria", sino que también debe ser impredecible incluso para un atacante que ha visto varios bloques de el keystream, una propiedad que estos generadores generales no garantizan.

## 4.2 Comparación con Stream Ciphers Modernos

### ¿Qué mejoras de seguridad ofrecen?

Los algoritmos contemporáneos como ChaCha20 y AES-CTR presentan mejoras importantes porque el keystream se genera utilizando primitivas criptográficas analizadas y estandarizadas y no a partir de un PRNG genérico. Esto les da resistencia a los ataques conocidos, impracticabilidad, seguridad formal basada en análisis matemáticos y revisión académica. Esto hace que el riesgo de poder reconstruir el flujo o hacer predicciones futuras del keystream se vea sensiblemente reducido.

### ¿Qué técnicas usan para evitar las vulnerabilidades de PRNG básicos?

Estos algoritmos utilizan mecanismos como nonces o IVs únicos por mensaje y contadores internos para garantizar que la keystream nunca se repita bajo la misma clave. A su vez, la keystream se obtiene mediante funciones criptográficas, que precisamente se encuentran diseñadas para resistir la correlación, predicción y ataques estructurales, evitando las debilidades de generadores pseudoaleatorios simples.

### ¿Cómo manejan la inicialización y el estado interno?

En ChaCha20 y AES-CTR, el estado interno se forma mediante la combinación de una clave secreta, un nonce único y un contador incremental, con el fin de que se puedan generar múltiples bloques diferenciados y no repetidos del keystream. Este diseño permite, además, separar claramente la clave del propio mecanismo de generación de flujo y garantiza que, aunque se cifren un gran número de mensajes con una misma clave, el uso adecuado de nonces diferentes impida volver a usar el mismo keystream, incrementando así la seguridad frente a ataques reales.

### Incluya referencias bibliográficas a sus fuentes.

Nir, Y., & Langley, A. (2015, May 1). ChaCha20 and Poly1305 for IETF Protocols. IETF. https://datatracker.ietf.org/doc/html/rfc7539

‌Dworkin, M. (2001). Recommendation for Block Cipher Modes of Operation Methods and Techniques. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf

‌Python. (2025). random — Generate pseudo-random numbers — Python 3.8.2 documentation. Docs.python.org. https://docs.python.org/3/library/random.html

‌