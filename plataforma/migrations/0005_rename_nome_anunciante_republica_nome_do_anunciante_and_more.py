# Generated by Django 4.1.4 on 2022-12-25 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_rename_descrição_republica_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='republica',
            old_name='nome_anunciante',
            new_name='nome_do_anunciante',
        ),
        migrations.RenameField(
            model_name='republica',
            old_name='regras_da_república',
            new_name='regras_da_republica',
        ),
    ]
