# Generated by Django 4.1.5 on 2023-01-12 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_republica_foto2_republica_foto3_republica_foto4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='republica',
            name='foto2',
        ),
        migrations.RemoveField(
            model_name='republica',
            name='foto3',
        ),
        migrations.RemoveField(
            model_name='republica',
            name='foto4',
        ),
        migrations.RemoveField(
            model_name='republica',
            name='foto5',
        ),
    ]