# Generated by Django 4.1.5 on 2023-01-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_remove_republica_foto1'),
    ]

    operations = [
        migrations.AddField(
            model_name='republica',
            name='imagem1',
            field=models.FileField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
