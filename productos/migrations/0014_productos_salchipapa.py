# Generated by Django 3.2.7 on 2023-05-24 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_remove_producto_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos_salchipapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('image1', models.ImageField(upload_to='productos', verbose_name='Imagen1')),
                ('precio', models.FloatField(null=True, verbose_name='precio')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Direccion Web')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoriasprod')),
            ],
            options={
                'verbose_name': 'producto_salchipapa',
                'verbose_name_plural': 'productos_salchipapas',
                'ordering': ['created'],
            },
        ),
    ]
