# Generated by Django 4.1.5 on 2023-01-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0010_republica_imagem1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='republica',
            name='imagem1',
        ),
        migrations.AddField(
            model_name='republica',
            name='foto1',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='republica',
            name='foto2',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='republica',
            name='foto3',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='republica',
            name='foto4',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='republica',
            name='foto5',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
