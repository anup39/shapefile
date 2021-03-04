# Generated by Django 3.0.4 on 2021-02-08 05:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_of', models.IntegerField()),
                ('width', models.IntegerField()),
                ('precision', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('srs_wkt', models.CharField(max_length=255)),
                ('geom_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom_point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('geom_multipoint', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
                ('geom_multilinestring', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('geom_multipolygon', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('geom_geometrycollection', django.contrib.gis.db.models.fields.GeometryCollectionField(blank=True, null=True, srid=4326)),
                ('shapefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateProject.Shapefile')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateProject.Attribute')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateProject.Feature')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='shapefile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateProject.Shapefile'),
        ),
    ]
