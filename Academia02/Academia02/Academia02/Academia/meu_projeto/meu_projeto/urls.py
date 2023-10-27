from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('autor/autor_edit/<int:id>/',views.autor_edit, name='autor_edit'),
    path('autor/autor_delete/<int:id>/',views.autor_delete, name='autor_delete'),
    path('autor_add/',views.autor_add, name='autor_add'),
    
    path('editora/editora_edit/<int:id>/',views.editora_edit, name='editora_edit'),
    path('editora/editora_delete/<int:id>/',views.editora_delete, name='editora_delete'),
    path('editora_add/',views.editora_add, name='editora_add'),
    path('editora/',views.editora, name='editora'),   
     
    path('formato/formato_edit/<int:id>/',views.formato_edit, name='formato_edit'),
    path('formato/formato_delete/<int:id>/',views.formato_delete, name='formato_delete'),
    path('formato_add/',views.formato_add, name='formato_add'),
    path('formato/',views.formato, name='formato'),  
      
    path('livro/livro_edit/<int:id>/',views.livro_edit, name='livro_edit'),
    path('livro/livro_delete/<int:id>/',views.livro_delete, name='livro_delete'),
    path('livro_add/',views.livro_add, name='livro_add'),
    path('livro/',views.livro, name='livro'),   
     
    path('autor/',views.autor, name='autor'),
    # path('autor/autor_edit/<int:id>/',views.autor_edit, name='autor_edit'),
]


