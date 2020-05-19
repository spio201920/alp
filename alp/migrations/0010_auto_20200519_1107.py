# Generated by Django 3.0.5 on 2020-05-19 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0009_auto_20200519_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['round_game', 'game_date']},
        ),
        migrations.AddField(
            model_name='match',
            name='game_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
