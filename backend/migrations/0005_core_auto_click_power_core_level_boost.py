# Generated by Django 4.0.5 on 2022-06-12 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_core_auto_click_power_remove_core_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='auto_click_power',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=10)),
                ('power', models.IntegerField(default=1)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'auto'), (0, 'casual')], default=0)),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.core')),
            ],
        ),
    ]
