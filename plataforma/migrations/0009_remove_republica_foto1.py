# Generated by Django 4.1.5 on 2023-01-12 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_remove_republica_foto2_remove_republica_foto3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='republica',
            name='foto1',
        ),
    ]