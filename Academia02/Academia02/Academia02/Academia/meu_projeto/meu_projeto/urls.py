"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('autor/',views.autor, name='autor'),
    # path('autor/autor_edit/<int:id>/',views.autor_edit, name='autor_edit'),
]


