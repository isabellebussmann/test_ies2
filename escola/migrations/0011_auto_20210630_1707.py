# Generated by Django 3.2.4 on 2021-06-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0010_auto_20210630_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='prova',
            field=models.ManyToManyField(to='escola.Prova'),
        ),
        migrations.DeleteModel(
            name='PerguntasProva',
        ),
    ]
