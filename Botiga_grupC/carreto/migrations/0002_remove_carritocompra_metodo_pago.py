# Generated by Django 4.2.1 on 2023-06-10 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritocompra',
            name='metodo_pago',
        ),
    ]
