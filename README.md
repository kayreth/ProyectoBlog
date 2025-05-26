# PrimeraPagina_Marrero

Este es un proyecto web en Django que simula un blog. Incluye:

- Herencia de plantillas HTML ✅
- Tres modelos (`Autor`, `Categoria`, `Post`) ✅
- Formularios para ingresar datos a cada uno ✅
- Un formulario para buscar posts por título ✅
- Página para ver todos los posts creados ✅

---

## ⚙️ Cómo ejecutar el proyecto

1. Crear entorno virtual y activarlo:
   ```
   python -m venv env
   env\Scripts\activate     (en Windows)
   ```

2. Instalar Django:
   ```
   pip install django
   ```

3. Ejecutar migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Iniciar el servidor:
   ```
   python manage.py runserver
   ```

---

## 🌐 Funcionalidades y rutas

| URL                 | Qué hace                          |
|---------------------|-----------------------------------|
| `/`                 | Página de inicio                  |
| `/nuevo-post/`      | Crear un nuevo post               |
| `/nuevo-autor/`     | Crear un nuevo autor              |
| `/nueva-categoria/` | Crear una nueva categoría         |
| `/buscar/`          | Buscar posts por título           |
| `/posts/`           | Ver todos los posts creados       |

---

## ✨ Extra

- Se usa `ModelForm` para facilitar los formularios.
- Todas las vistas usan plantillas con herencia (`base.html`).

---

## 📁 Estructura del proyecto

```
PrimeraPagina_Marrero/
├── env/                     ← Entorno virtual (no subir)
├── mi_blog/
│   ├── manage.py
│   ├── mi_blog/             ← Configuración principal
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
```

---

## ✅ Recomendación

Agregá también un archivo `.gitignore` para ignorar el entorno virtual y archivos temporales:

```
env/
__pycache__/
db.sqlite3
*.pyc
```
