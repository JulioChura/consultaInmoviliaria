# Generated by Django 5.1.4 on 2024-12-17 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lindavista', '0002_rename_consulta_sql_lnpatron_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lnpatron',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='lnpatron',
            name='fecha_creacion',
        ),
    ]