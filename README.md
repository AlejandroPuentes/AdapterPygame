# AdapterPygame

## Integrantes:

- Brayan Alejandro Puentes Camargo  - 20181020044
- Johnatan Guillermo Ruiz Bautista  - 20181020034
- Juan Camilo Ramírez Rátiva        - 20181020089

### Diagrama UML

![alt text](https://github.com/wthoutjc/Serenata/blob/master/BandaUML2.0.png)

### <center> Descripcion Del Programa </center>0
<p align= "Justify">Este programa simula el movimiento de dos objetos 2d: uno original y otro adaptado, que pueden interactuar bajo controles de movimiento en sentido derecha e izquierda. Aplicativo creado con base en el patrón estructural adapter.</p>

**Objeto Original**
![alt text](https://github.com/jgruizba/AdapterPygame/blob/master/bomber.jpeg)

**Objeto Adaptado**
![alt text](https://github.com/jgruizba/AdapterPygame/blob/master/origina.jpeg)

<p align= "Justify">Para escoger el objeto a usar debe dirigirse a Main.py y donde esta definida la variable character escoger el tipo: MainCharacter() que representa el objeto original o AdapterCharacter() que representa el objeto adaptado.</p>

### **Requerimientos**
<p align= "Justify">Programa diseñado en Python 3.7.3, para poder ejecutar el código de manera correcta asegúrese de tener instalado el módulo de pygame.</p>

### Principios de diseño
1.**Principio de Responsabilidad Única:**

<p align= "Justify">Este principio se basa en que una clase tiene una, y solo una razón para cambiar, como podemos observar el programa deja a cada una de sus clases una única tarea que le identifica, manteniendo así una única responsabilidad, y lograr tener bajo acoplamiento las clases.</p>

2.**Principio de Abierto – Cerrado:**

<p align= "Justify">Este principio trata sobre que las clases deberían estar sujetas a las extensiones, pero cerradas para las modificaciones de código fuente, es por eso que nuestro código en pro de cumplir este principio observamos que la clase “AdapterCharacter” se instancia en la clase “Main”, sin afectar o modificar el funcionamiento de la clase, en otras palabras, el diseño del programa esta abierto a la extensibilidad y cerrado a la modificación del código fuente.</p>

3.**Principio de Sustitución de Liskov:**
<p align= "Justify">En nuestro programa podemos observar como este principio es implementando debido a las herencias múltiples que se presentan en Character, en la FabricaAbstracta, debido a que las clases derivadas pueden ser tratadas como la propia clase base, lo que nos permite interpretar que los objetos pueden ser reemplazados por instancias de sus subtipos sin alterar el correcto funcionamiento del sistema.</p>

## Patrones de diseño.

1.**Abstract Factory:**

<p align= "Justify">Podemos observar que la implementación de este patrón esta dado en las fabricas de los sprites para la secuencia de imágenes y animaciones de los objetos 2d.</p>

2.**Adapter:**

<p align= "Justify">El uso de este patrón estructural se implementa para poder usar los métodos del personaje foráneo en nuestro código, y así permitir ejecutar los movimientos en el módulo de pygame, sin tener que hacer cambios en la interfaz.</p> 

