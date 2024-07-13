from django.urls import path
from .views import excel_writer, excel_reader

# app_name = 'user'
urlpatterns = [
    path('/write', excel_writer, name='write'),
    path('/read', excel_reader, name='read'),
]