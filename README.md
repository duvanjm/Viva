# Search Stories

Aplicación que que consume la API de Hacker-news para consultar los últimos post. La aplicación recibe un indice i, un numero máximo de hisotrias n y devuelve los detalles de las n hisotiras a partir de la hisotria i.

## Requisitos :pencil:

- Python
- Django

## Instalacion :wrench:

- Clona el repositorio
   ```bash
   $ git clone https://github.com/duvanjm/Viva.git
   $ cd Viva_air/
   ```
   Ejecute el servidor de django con en comando "python3 manage.py runserver"

## Uso :trophy:

- Start the API:

  ```bash
  $ cd backend/
  $ python3 manage.py runserver
  ```

Para consultar las top stories ingrese al endpoint:

  ```bash
  /viva/stories
  ```
Allí la aplicación consultará la lista de las principales historias y lo guardará en cache.

Para concultar las historias ingrese al endpoint: 
  ```bash
  /viva/stories/i/n
  ``` 
y especifique el indice y el numero de historias, estas se guardaran en cahce por 10 segundos.

Para borar el cache, ingrese al endpoint: 
  ```bash
  /viva/stories/delete 
  ```

Ahora puedes usar la aplicacion en [localhost:8000/viva/stories/0/1](localhost:8000/viva/stories/0/1) :video_game:
