# Generated by Django 3.2.4 on 2021-06-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oracle', '0004_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('nomCategoria', models.CharField(max_length=25)),
                ('idcategoria', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
