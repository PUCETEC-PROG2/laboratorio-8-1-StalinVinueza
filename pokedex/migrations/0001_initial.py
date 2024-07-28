# Generated by Django 4.2 on 2024-07-28 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('A', 'Agua'), ('E', 'Eléctrico'), ('T', 'Tierra'), ('P', 'Planta'), ('F', 'Fuego')], max_length=30)),
                ('weight', models.DecimalField(decimal_places=2, default=1, max_digits=4)),
                ('height', models.DecimalField(decimal_places=2, default=1, max_digits=4)),
                ('picture', models.ImageField(upload_to='pokemon_images')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.trainer')),
            ],
        ),
    ]
