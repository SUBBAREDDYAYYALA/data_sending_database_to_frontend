from django.shortcuts import render

from app.models import *

# Create your views here.
def database(request):

    so = sports.objects.all()

    po = player.objects.all()

    d={'so':so,'po':po}

    return render(request,'database.html',d)