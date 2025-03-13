# Programacion Basica
## Adan Eduardo Lopez Rodriguez
### unidad 2.	
¿Qué tipo de clasificación de software hay?  
 Clasificación por Función
Software de Sistema:
Sistema Operativo: Coordina y controla el hardware y otros programas. Ejemplos: Windows, macOS, Linux.
Controladores de Dispositivo: Permiten la comunicación entre el sistema operativo y los dispositivos hardware. Ejemplos: controladores de impresoras, controladores de tarjetas gráficas.
Utilidades del Sistema: Realizan tareas de mantenimiento y soporte. Ejemplos: antivirus, herramientas de copia de seguridad.

Software de Aplicación:

Software de Productividad: Facilita tareas cotidianas. Ejemplos: Microsoft Office, Google Workspace.

Software de Diseño y Multimedia: Utilizado para la creación y edición de contenido multimedia. Ejemplos: Adobe Photoshop, AutoCAD.

Software Educativo: Diseñado para facilitar el aprendizaje. Ejemplos: Duolingo, Khan Academy.

Software de Programación:

Editores de Texto y Entornos de Desarrollo: Herramientas para escribir y depurar código. Ejemplos: Visual Studio, IntelliJ IDEA.

Compiladores e Intérpretes: Traducen el código fuente a código máquina. Ejemplos: GCC, Python.

Clasificación por Distribución
Software de Código Abierto (Open Source):

El código fuente está disponible para ser modificado y distribuido libremente. Ejemplos: Linux, Apache.

Software Propietario (Closed Source):

El código fuente no está disponible para el público y su uso está restringido por licencias. Ejemplos: Windows, Microsoft Office.

Software Gratuito (Freeware):

Se puede descargar y usar sin costo, pero usualmente es propietario. Ejemplos: Skype, Adobe Acrobat Reader.

Software de Prueba (Shareware):

Se puede usar de manera gratuita por un tiempo limitado o con funcionalidades restringidas, después de lo cual se debe pagar. Ejemplos: WinRAR, algunas versiones de antivirus.

Software Libre (Free Software):

Similar al software de código abierto, pero con un enfoque en las libertades del usuario para usar, estudiar, modificar y distribuir el software. Ejemplos: GNU Emacs, LibreOffice.

Clasificación por Uso
Software Vertical:

Diseñado para un sector específico de la industria. Ejemplos: software para gestión hospitalaria, software para la industria bancaria.

Software Horizontal:

Utilizable en diversas industrias y contextos. Ejemplos: software de contabilidad, software de gestión de recursos humanos
2.	¿Qué es un algoritmo?
Un algoritmo es un conjunto de pasos o instrucciones precisas diseñadas para realizar una tarea específica o resolver un problema. Los algoritmos se utilizan en diversas áreas, como la informática, las matemáticas, la ingeniería y la vida cotidiana
3.	¿Que es un lenguaje de programación? 
Un lenguaje de programación es un conjunto de reglas y sintaxis que permite a los programadores escribir instrucciones que una computadora puede entender y ejecutar. Estos lenguajes sirven como intermediarios entre los humanos y las máquinas, facilitando la creación de programas y aplicaciones.
4.	¿Qué es un paradigma de programación? ´
Un paradigma de programación es un enfoque o estilo particular para escribir programas y resolver problemas usando un lenguaje de programación. Los paradigmas de programación proporcionan diferentes maneras de organizar y estructurar el código, y cada uno tiene sus propias características y ventajas. Aquí algunos de los paradigmas más comunes:

Paradigma Imperativo: Este enfoque se basa en secuencias de instrucciones que cambian el estado del programa. Lenguajes como C, C++ y Java siguen este paradigma.

Paradigma Declarativo: Se centra en describir qué debe hacer el programa, sin especificar cómo hacerlo. Ejemplos incluyen SQL y lenguajes de programación funcional como Haskell.

Paradigma Orientado a Objetos: Organiza el código en “objetos” que contienen datos y métodos. Lenguajes como Java, Python y C++ siguen este paradigma.

Paradigma Funcional: Se basa en la evaluación de funciones y evita estados mutables y efectos secundarios. Ejemplos incluyen Haskell, Lisp y Scala.

Paradigma Lógico: Se basa en la lógica formal y la resolución de problemas a través de reglas lógicas. Prolog es un lenguaje que sigue este paradigma.
5.	¿Cuál es la diferencia de un lenguaje interpretado y uno compilado?
Lenguaje Interpretado
Ejecución: El código fuente se ejecuta línea por línea, directamente a través de un intérprete.

Ventajas:

Facilita la depuración (debugging) porque puedes ejecutar y probar el código rápidamente.

Mayor portabilidad, ya que no depende de una compilación previa.

Desventajas:

Generalmente más lento en ejecución, porque cada línea debe ser traducida en tiempo real.

Ejemplos: Python, JavaScript, Ruby.

Lenguaje Compilado
Ejecución: El código fuente se traduce completamente a código máquina a través de un compilador antes de su ejecución. El resultado es un archivo ejecutable.

Ventajas:

Mayor velocidad de ejecución, ya que el código ya está en formato que la máquina entiende.

Generalmente más eficiente en términos de uso de recursos.

Desventajas:

El proceso de compilación puede ser más lento y complejo.

Menor flexibilidad para cambios rápidos y pruebas inmediatas.

Ejemplos: C, C++, Java (aunque Java utiliza una combinación de compilación e interpretación a través de la máquina virtual Java).
6.	¿Qué es un lenguaje de alto nivel y de bajo nivel?
Lenguajes de Alto Nivel
Abstracción: Proporcionan una mayor abstracción y son más cercanos al lenguaje humano, lo que los hace más fáciles de leer y escribir.

Ventajas:

Facilitan el desarrollo rápido de software.

Son portables entre diferentes sistemas operativos y hardware.

Incluyen características avanzadas como la gestión automática de memoria y bibliotecas extensas.

Desventajas:

Suelen ser menos eficientes en términos de rendimiento y uso de recursos comparados con los lenguajes de bajo nivel.

Ejemplos: Python, Java, C#, JavaScript, Ruby.

Lenguajes de Bajo Nivel
Abstracción: Están más cerca del lenguaje máquina y proporcionan menos abstracción, lo que les permite un control más directo del hardware.

Ventajas:

Ofrecen un rendimiento y eficiencia superiores.

Permiten un control preciso sobre los recursos del sistema, como la memoria y el procesador.

Desventajas:

Son más difíciles de aprender y escribir debido a su complejidad y menor legibilidad.

Son menos portables, ya que están más ligados a la arquitectura específica del hardware.

Ejemplos: Lenguaje ensamblador (Assembly), lenguajes máquina (código binario).

### unidad 3
operador
'if':La palabra clave "if" es una estructura fundamental en la mayoría de los lenguajes de programación. Sirve para tomar decisiones basadas en una condición específica. Si la condición se cumple (es verdadera), se ejecuta un bloque de código; de lo contrario, dicho bloque se ignora, y puedes definir una acción alternativa con un "else".

Por ejemplo, en Python:

python
x = 10
if x > 5:
    print("x es mayor que 5")  # Esto se ejecuta porque la condición es verdadera.
else:
    print("x es menor o igual que 5")

'else':es complementaria al if si esta no se cumple  

'elif': que significa "else if". Sirve para evaluar una nueva condición cuando la primera del if no se cumple. Esto permite manejar múltiples alternativas de una forma más ordenada y clara que usar varios bloques separados de if.

Por ejemplo:

python
calificacion = 85

if calificacion >= 90:
    print("Obtuviste una A.")
elif calificacion >= 80:
    print("Obtuviste una B.")
elif calificacion >= 70:
    print("Obtuviste una C.")
else:
    print("Necesitas mejorar.")

'while':
El "while" en Python es una estructura de control que se utiliza para ejecutar repetidamente un bloque de código mientras una condición sea verdadera. Es ideal cuando no sabes de antemano cuántas veces necesitas repetir algo y quieres que el programa siga funcionando bajo ciertas condiciones.

Por ejemplo:

python
contador = 1

while contador <= 5:
    print(f"Este es el número {contador}")
    contador += 1  # Incrementa el contador en 1
En este caso:

La condición es contador <= 5. Mientras esta sea verdadera, el bloque se seguirá ejecutando


En
'for':El "for" en Python se utiliza para iterar sobre elementos de una secuencia (como una lista, una tupla, un diccionario, un conjunto o una cadena de texto) o para realizar una acción un número específico de veces. Es ideal cuando sabes cuántas veces necesitas repetir algo o cuando necesitas recorrer elementos uno por uno.

Por ejemplo, para iterar sobre una lista:

python
frutas = ["manzana", "plátano", "cereza"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")
Esto imprimirá:

Me gusta la manzana
Me gusta el plátano
Me gusta la cereza
También puedes usar el "for" con un rango de números usando la función range():

python
for numero in range(1, 6):  # Itera desde 1 hasta 5 (6 no está incluido)
    print(f"Este es el número {numero}")
Esto imprimirá:

Este es el número 1
Este es el número 2
Este es el número 3
Este es el número 4
Este es el número 5
El bucle for es muy versátil y se puede combinar con instrucciones como "break" (para salir del bucle) y "continue" (para saltar a la siguiente iteración).


Libtrerias:En programación, una librería es un conjunto de funciones, clases, métodos o recursos predefinidos que puedes utilizar en tus programas para ahorrar tiempo y esfuerzo. En lugar de escribir todo el código desde cero, puedes simplemente importar una librería y aprovechar el trabajo ya realizado por otros programadores.

Por ejemplo, en Python, hay muchas librerías populares que se usan para diferentes propósitos:

math: Proporciona funciones matemáticas como sqrt() (raíz cuadrada) o sin() (seno).

random: Permite generar números aleatorios.

pandas: Es útil para el análisis y manejo de datos.

matplotlib: Se usa para crear gráficos y visualizaciones.

Tipos de datos:
entero = 5
flotante = 1.2
cadena = "Ed Flores"
booleano = True

switch:


En Python, no existe una estructura "switch" o "case" como en otros lenguajes de programación (por ejemplo, C, C++ o JavaScript). Sin embargo, puedes lograr un comportamiento similar utilizando un diccionario con funciones o combinando condiciones con if, elif, else.

Aquí tienes un ejemplo usando un diccionario para simular un switch-case:

python
def caso1():
    return "Elegiste el caso 1."

def caso2():
    return "Elegiste el caso 2."

def caso_default():
    return "Este es el caso por defecto."

Diccionario que actúa como un switch
opciones = {
    1: caso1,
    2: caso2
}
Simulamos el switch
eleccion = 3
resultado = opciones.get(eleccion, caso_default)()  # Si no encuentra la clave, usa caso_default
print(resultado)
Este ejemplo simula un "switch-case", donde opciones.get(eleccion, caso_default) busca la opción correspondiente o ejecuta una función por defecto si no se encuentra la clave.
