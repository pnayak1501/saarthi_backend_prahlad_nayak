"""saarthi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from saarthiApp import views

urlpatterns = [
    path('api/external-books', views.external_book), #for external books
    path('api/v1/books', views.create_read_book),  #Creating a book and displaying all books
    path('api/v1/books/<int:id>/update', views.update_book), # Updating a book attributes
    path('api/v1/books/<int:id>', views.delete_show_book),  #show and delete a particular book
]
