from django.contrib import admin

# Register your models here.

from .models import Autor,Editora,Formato,Livro

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Formato)
admin.site.register(Livro)
