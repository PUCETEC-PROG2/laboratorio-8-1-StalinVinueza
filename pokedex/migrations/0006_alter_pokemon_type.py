# Generated by Django 4.2 on 2024-07-29 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('Planta', 'Planta'), ('Fuego', 'Fuego'), ('Tierra', 'Tierra'), ('Agua', 'Agua'), ('Eléctrico', 'Eléctrico')], max_length=30),
        ),
    ]
