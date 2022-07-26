# Generated by Django 4.0.6 on 2022-07-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Anotacao',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
