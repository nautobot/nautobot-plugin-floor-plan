# Generated by Django 3.2.25 on 2024-08-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_floor_plan", "0007_add_axis_origin_seed"),
    ]

    operations = [
        migrations.AddField(
            model_name="floorplan",
            name="x_axis_step",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="floorplan",
            name="y_axis_step",
            field=models.IntegerField(default=1),
        ),
    ]
