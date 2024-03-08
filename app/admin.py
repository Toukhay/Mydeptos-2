from django.contrib import admin
from .models import Localidad, Agente, Departamento, Foto, Usuario
# esta seccion nos permite registrar los modelos para que sean visibles en el panel de administracion
# Register your models here.

admin.site.register(Localidad)
admin.site.register(Agente)
admin.site.register(Departamento)
admin.site.register(Foto)
admin.site.register(Usuario)
