from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

class MiLaboratorio(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    ordering = ('id',)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ('id',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'anio_fabricacion', 'p_costo', 'p_venta')
    ordering = ('id',)
    list_filter = ('nombre', 'laboratorio')

    def anio_fabricacion(self, obj):
        return obj.f_fabricacion.year

    anio_fabricacion.short_description = 'f_fabricacion'

admin.site.register(DirectorGeneral, DirectorAdmin)
admin.site.register(Laboratorio, MiLaboratorio)
admin.site.register(Producto, ProductoAdmin)
