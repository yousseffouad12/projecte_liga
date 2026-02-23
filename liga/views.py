from django.shortcuts import render
from .models import Equipo

def index(request):
    # Agafem tots els equips de la base de dades
    equips = Equipo.objects.all()
    # Enviem els equips al fitxer HTML (template)
    return render(request, 'liga/index.html', {'equips': equips})
