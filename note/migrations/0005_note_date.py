# Generated by Django 4.0.6 on 2022-07-26 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_note_delete_anotacao_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
