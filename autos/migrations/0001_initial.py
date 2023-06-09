# Generated by Django 4.1.7 on 2023-04-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
