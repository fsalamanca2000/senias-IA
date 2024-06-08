from django.shortcuts import render
from django.http import JsonResponse
from .models import Señas

def index(request):
    return render(request, 'recognition/index.html')
def obtener_señas(request):
    señas = Señas.objects.all()
    señas_data = [{'name': seña.name, 'image': seña.image.url} for seña in señas]
    return JsonResponse(señas_data, safe=False)

