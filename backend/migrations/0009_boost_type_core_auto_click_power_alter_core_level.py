# Generated by Django 4.0.5 on 2022-06-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_boost_level_alter_core_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'casual'), (1, 'auto')], default=0),
        ),
        migrations.AddField(
            model_name='core',
            name='auto_click_power',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
