# Proyecto Urban Grocers 

Este proyecto contiene pruebas automatizadas para la creación de kits. Las pruebas están diseñadas para validar varios casos de uso y asegurar que la API maneje correctamente tanto las solicitudes válidas como las no válidas

Requisitos

- Python 3.x
- requests
- pytest
- Documentación de la API

Instalaciones 
1. Descarga de python
2. Descarga de Pytest desde PyCharm
3. Descarga de Git
4. Descarga de paquete request, desde el comando pip install
5. Clonar el repositorio

Contenido 
El proyecto contiene 6 carpetas, entre las cuales esta:
1. Configuration.py
   * Dentro de este se encuentran las configuraciones para el proyecto en donde se almacenan las rutas para la documentación de la API.
2. data.py
   * Dentro de este se almacena la información que se enviara en las solicitudes, como el cuerpo y el encabezado.
3. sender_stand_request.py
   * Dentro de este se importarán los documentos almacenados dentro de las dos carpetas anteriores y con el paquete anteriormente descargado,los cuales son las funciones para enviar solicitudes a la API.
4. create_kit_name_kit_test.py
   * Dentro de este se encuentra las pruebas para validar la creación de kits
5. .gitignore
   * En este se guardan archivos para que Git los descarte.
6. README.md
   * El cual guarda la descripción del proyecto.

Información adicional 

* Asegúrate de tener un entorno virtual configurado para instalar las dependencias. 
* La URL y las rutas de la API están configuradas en el archivo configuration.py. 
* La creación de usuario y kits requiere un token de autenticación que se obtiene al crear un nuevo usuar

