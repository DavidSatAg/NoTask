# Generated by Django 4.0.6 on 2022-07-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='data_tarefa',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data/hora'),
        ),
    ]
