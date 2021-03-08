# Generated by Django 3.1.6 on 2021-03-08 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210308_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 11, 13, 2, 806135, tzinfo=utc)),
        ),
    ]