# Generated by Django 3.1.6 on 2021-02-21 10:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_todo_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateTimeFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='modified_at',
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 10, 35, 9, 104578, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='todo',
            name='datetimefields_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todoapp.datetimefields'),
            preserve_default=False,
        ),
    ]