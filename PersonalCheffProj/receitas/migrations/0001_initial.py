# Generated by Django 3.2 on 2022-10-01 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receitas', models.CharField(max_length=180)),
                ('video', models.CharField(max_length=88)),
                ('modo_preparo', models.TextField()),
                ('ingredientes', models.TextField()),
                ('nota', models.IntegerField()),
                ('data_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
