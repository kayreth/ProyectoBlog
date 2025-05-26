from django.contrib import admin
from .models import Autor, TipoComida, Receta

admin.site.register(Autor)
admin.site.register(TipoComida)
admin.site.register(Receta)