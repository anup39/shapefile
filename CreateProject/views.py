from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django import forms
from .shapefileIO import *



class ImportShapefileForm(forms.Form):
    import_file = forms.FileField(label="Select a Zipped Shapefile")



def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html",{'shapefiles' : shapefiles})



def import_shapefile(request):
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request,"import_shapefile.html",{'form' : form,'errMsg' : None})

    elif request.method == "POST":
        errMsg = None # initially.
        form = ImportShapefileForm(request.POST,request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            errMsg = shapefileIO.import_data(shapefile)
            
            if errMsg == None:
                 return HttpResponseRedirect("list_of_shapefiles")
        return render(request,"import_shapefile.html",{'form' : form,'errMsg' : errMsg})