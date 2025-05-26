# PrimeraPagina_Marrero

Este es un proyecto web en Django que simula un blog de recetas. 

Incluye:

.- Herencia de plantillas HTML
.- Tres modelos ('Autor', 'Tipo de Comida', 'Receta')
.- Formularios para ingresar datos
.- Un formulario para buscar y ver recetas por título
.- Página para ver todos los recetas creados

## ¿Cómo ejecutar el proyecto?

1. Crear entorno virtual y activarlo:   
   python -m venv env
   env\Scripts\activate (en Windows)

2. Instalar Django:
   pip install django

3. Ejecutar migraciones:
   python manage.py makemigrations
   python manage.py migrate

4. Iniciar el servidor:
   python manage.py runserver

## Funcionalidades y rutas

| URL                 | Qué hace                          |
|---------------------|-----------------------------------|
| '/'                 | Página de inicio                  |
| '/nueva-receta/'    | Crear un nueva receta             |
| '/crear-autor/'     | Crear un nuevo autor              |
| '/nuevo-tipo/'      | Crear un nuevo tipo de comida     |
| '/buscar/'          | Buscar y ver recetas por título   |
| '/posts/'           | Ver todos las recetas creadas     |

## Comentarios

.- Se usa 'ModelForm' para facilitar los formularios.
.- Todas las vistas usan plantillas con herencia ('base.html').

## Estructura del proyecto

PrimeraPagina_Marrero/
├── env/
├── mi_blog/
│   ├── manage.py
│   ├── mi_blog/
│   ├── blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/blog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── formulario.html
│   │       ├── buscar.html
│   │       └── listar_posts.html

## Recomendación

Agregá también un archivo `.gitignore` para ignorar el entorno virtual y archivos temporales:

```
env/
__pycache__/
db.sqlite3
*.pyc
```
