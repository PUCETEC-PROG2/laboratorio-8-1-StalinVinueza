# Generated by Django 4.2 on 2024-07-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('EElectrico', 'Eléctrico'), ('Fuego', 'Fuego'), ('Agua', 'Agua'), ('Planta', 'Planta'), ('Tierra', 'Tierra')], max_length=30),
        ),
    ]
