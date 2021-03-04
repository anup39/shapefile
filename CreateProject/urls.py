from django.urls import path

from . import views

urlpatterns = [
  path('list/', views.list_shapefiles, name='list_shapefiles'),
  path("import/",views.import_shapefile,name="import")
]