# Generated by Django 4.2.3 on 2023-08-05 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('etapa', models.IntegerField()),
                ('km', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('victorias', models.IntegerField()),
                ('podios', models.IntegerField()),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('ciclista_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion.ciclista')),
                ('posicion', models.IntegerField()),
                ('tiempo', models.DateField()),
            ],
            bases=('aplicacion.ciclista',),
        ),
    ]
