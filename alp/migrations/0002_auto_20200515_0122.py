# Generated by Django 3.0.5 on 2020-05-14 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league', to='alp.League'),
        ),
    ]
