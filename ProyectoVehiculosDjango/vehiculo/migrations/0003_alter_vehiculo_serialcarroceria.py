# Generated by Django 5.1.3 on 2024-12-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_categoria_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='serialCarroceria',
            field=models.CharField(max_length=50, verbose_name='Serial Carroceria'),
        ),
    ]
