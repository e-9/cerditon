# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PigData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('Age', models.IntegerField(default=0, verbose_name=b'Edad')),
                ('Height', models.IntegerField(default=0, verbose_name=b'Altura')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PigStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.FloatField(default=0.0, verbose_name=b'Peso')),
                ('fat_percentage', models.FloatField(default=0.0, verbose_name=b'Porcentage de grasa')),
                ('total_body_water', models.FloatField(default=0.0, verbose_name=b'Porcentage de liquidos')),
                ('body_mass_index', models.FloatField(default=0.0, verbose_name=b'Porcentage de masa muscular')),
                ('bone_percentage', models.FloatField(default=0.0, verbose_name=b'Porcentage de masa osea')),
                ('muscle_percentage', models.FloatField(default=0.0, verbose_name=b'Porcentage de masa corporal')),
                ('kilocalories', models.FloatField(default=0.0, verbose_name=b'Kilocalorias')),
                ('ideal_weight', models.FloatField(default=0.0, verbose_name=b'Peso ideal')),
                ('week', models.IntegerField(default=0, verbose_name=b'Semana')),
                ('pig_data', models.ForeignKey(to='cerdoton_app.PigData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
