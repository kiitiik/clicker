# Generated by Django 4.0.5 on 2022-06-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_boost_type_remove_core_auto_click_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]