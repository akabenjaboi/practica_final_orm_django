from django.urls import path 
from . import views

urlpatterns = [
    path('labs/', views.mostrarLab, name='mostrar_laboratorios'),
    path('insertarlab/', views.insertarLab, name='insertar_laboratorios'),
    path('editarLab/<int:laboratorio_id>/', views.editarLab ,name='actualizar_laboratorio'),
    path('eliminar_laboratorio/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),

]