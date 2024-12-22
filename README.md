# Proyecto de Búsqueda en Lenguaje Natural con Django y Vue.js

Este proyecto permite realizar consultas en lenguaje natural a una base de datos de viviendas. Utilizando un enfoque innovador con **Django** y **Vue.js**, se facilita la búsqueda de propiedades a través de frases como "Busco un piso en el centro" o "Deseo una casa con 3 habitaciones".

## Tecnologías utilizadas

Este proyecto está compuesto por las siguientes tecnologías:

- **Django**: Framework para desarrollo web basado en Python. Gestiona la API que recibe las consultas y ejecuta las búsquedas en la base de datos.
- **Vue.js**: Framework progresivo de JavaScript utilizado para el frontend. Permite una experiencia de usuario interactiva y dinámica.
- **Tailwind CSS**: Framework de CSS para diseñar la interfaz de usuario de manera rápida y moderna.
- **Axios**: Librería de JavaScript para realizar peticiones HTTP desde el frontend a la API backend.
- **Cloudinary**: Para gestionar las imágenes de las propiedades de forma eficiente en la web.
- **MySQL**: Base de datos para almacenar las propiedades de la inmobiliaria.

## Funcionalidades

1. **Consulta en Lenguaje Natural**: El usuario puede escribir frases de búsqueda como "Busco un piso con 3 habitaciones" y el sistema las interpreta para hacer una búsqueda en la base de datos.
2. **Filtros de Búsqueda**: Las consultas se realizan con filtros automáticos por tipo de propiedad, zona, número de dormitorios, etc.
3. **Interfaz Intuitiva**: Con Vue.js y Tailwind CSS, la página proporciona una interfaz de usuario limpia y fácil de usar.
4. **Resultados Interactivos**: Muestra los resultados de búsqueda de manera interactiva y amigable.

## Imágenes de la Web

### Página principal con formulario de búsqueda

![Formulario de búsqueda](./images/formulario_busqueda.png)

### Resultados de búsqueda

![Resultados](./images/resultados_busqueda.png)

## Instrucciones para ejecutar el proyecto

### Backend (Django)
1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu_usuario/proyecto-lenguaje-natural.git
    cd proyecto-lenguaje-natural/backend
    ```

2. Crea un entorno virtual e instálalo:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa env\Scripts\activate
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Crea un superusuario (si lo necesitas):
    ```bash
    python manage.py createsuperuser
    ```

5. Inicia el servidor:
    ```bash
    python manage.py runserver
    ```

### Frontend (Vue.js)
1. Navega a la carpeta del frontend:
    ```bash
    cd frontend
    ```

2. Instala las dependencias:
    ```bash
    npm install
    ```

3. Inicia el servidor de desarrollo:
    ```bash
    npm run serve
    ```

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b nueva-caracteristica`).
3. Haz tus cambios y realiza un commit (`git commit -am 'Agregué nueva característica'`).
4. Haz push a tu rama (`git push origin nueva-caracteristica`).
5. Crea un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
