# Generated by Django 3.1.7 on 2021-03-12 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2021, 3, 13), verbose_name='登録日'),
        ),
    ]
