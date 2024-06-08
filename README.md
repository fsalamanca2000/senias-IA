# Escaner de objetos con traducción en lenguaje de señas

## Autores
- Juan Felipe Salamanca González (506222704)
- Derly Yanneth Rojas Herrera (506221072)

## Información previa

Para el correcto funcionamiento del proyecto es necesaria la instalación de las librerías. Al clonar el repositorio, debes abrir una terminal y en la ruta de la carpeta llamada `objeto_señas` ejecutar el siguiente comando:

```bash
pip install -r requeriments.txt
```
Tras finalizar este proceso, ya puedes ejecutar correctamente el proyecto.

Ejecución del proyecto
Para iniciar el uso, tienes que levantar el servidor proporcionado por Django utilizando el siguiente comando:
```bash
python manage.py runserver localhost:3001
```
Con esto, abre la ruta en tu navegador oprimiendo Control + Click encima de la ruta que se genera en la terminal, donde se mostrarán todas las rutas del proyecto.

Ahora debes ingresar a la ruta /señas y se mostrará la interfaz.

Uso de la interfaz
Botón detectar objetos: Este botón activará el modelo de IA que reconocerá los objetos que puede ver tu cámara y los categorizará mostrándote un recuadro con lo que entiende que es el modelo.
Botón traducir objeto: Este botón recopila la información detectada por el otro botón y despliega un div con la información de la base de datos de señas y muestra la seña correspondiente.
Base de datos
La base de datos de Django nos permitió registrar señas como objetos, donde uno de sus atributos es el nombre del objeto al que representa la seña y una imagen con la guía para realizarla.

Para agregar más señas, dirígete a la ruta /admin, usa las credenciales y haz click en señas, luego haz click en añadir, donde podrás crear el objeto seña con su nombre e imagen. Vale aclarar que esta función solo la pueden realizar usuarios con los permisos asignados.
