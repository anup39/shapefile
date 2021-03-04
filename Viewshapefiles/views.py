from django.http import HttpResponse
from django.shortcuts import render
from naxamapper.CreateProject.models import Shapefile



def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html",{'shapefiles' : shapefiles}