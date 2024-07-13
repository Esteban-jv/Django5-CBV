from django.urls import path
from .views import csv_read, csv_read_dic, csv_write, csv_write_dic

# app_name = 'user'
urlpatterns = [
    path('/read', csv_read, name='read'),
    path('/dread', csv_read_dic, name='dread'),
    path('/write', csv_write, name='write'),
    path('/dwrite', csv_write_dic, name='dwrite'),
]