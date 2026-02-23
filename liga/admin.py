from django.contrib import admin
from .models import Equipo, Jugador

# Esto es lo que hace que aparezcan en el panel
admin.site.register(Equipo)
admin.site.register(Jugador)
