# Generated by Django 3.2.4 on 2021-06-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0009_perguntasprova'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perguntasprova',
            name='prova',
        ),
        migrations.AddField(
            model_name='perguntasprova',
            name='prova',
            field=models.ManyToManyField(to='escola.Prova'),
        ),
    ]
