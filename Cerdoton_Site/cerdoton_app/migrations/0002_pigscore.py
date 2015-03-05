# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerdoton_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PigScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField(default=0, verbose_name=b'Semana')),
                ('thumbs_up', models.IntegerField(default=0, verbose_name=b'Paloma')),
                ('thumbs_down', models.IntegerField(default=0, verbose_name=b'Tache')),
                ('pig_data', models.ForeignKey(to='cerdoton_app.PigData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
