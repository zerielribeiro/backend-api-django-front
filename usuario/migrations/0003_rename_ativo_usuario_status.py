# Generated by Django 3.2.6 on 2021-08-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_ativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='ativo',
            new_name='status',
        ),
    ]
