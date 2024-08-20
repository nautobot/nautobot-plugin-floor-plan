# Generated by Django 3.2.16 on 2023-03-02 21:23

import uuid

import django.core.serializers.json
import django.core.validators
import django.db.models.deletion
import nautobot.extras.models.mixins
import nautobot.extras.models.statuses
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("extras", "0047_enforce_custom_field_slug"),
        ("dcim", "0014_location_status_data_migration"),
    ]

    operations = [
        migrations.CreateModel(
            name="FloorPlan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("x_size", models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ("y_size", models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                (
                    "tile_width",
                    models.PositiveSmallIntegerField(
                        default=100, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "tile_depth",
                    models.PositiveSmallIntegerField(
                        default=100, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "location",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="floor_plan", to="dcim.location"
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["location___name"],
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="FloorPlanTile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                (
                    "x_origin",
                    models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
                ),
                (
                    "y_origin",
                    models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
                ),
                (
                    "x_size",
                    models.PositiveSmallIntegerField(
                        default=1, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "y_size",
                    models.PositiveSmallIntegerField(
                        default=1, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                ("rack_orientation", models.CharField(blank=True, max_length=10)),
                (
                    "floor_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tiles",
                        to="nautobot_floor_plan.floorplan",
                    ),
                ),
                (
                    "rack",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="floor_plan_tile",
                        to="dcim.rack",
                    ),
                ),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="nautobot_floor_plan_floorplantile_related",
                        to="extras.status",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["floor_plan", "y_origin", "x_origin"],
                "unique_together": {("floor_plan", "x_origin", "y_origin")},
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
    ]
