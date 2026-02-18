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