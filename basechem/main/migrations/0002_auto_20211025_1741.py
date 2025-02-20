# Generated by Django 3.2.7 on 2021-10-25 21:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import basechem.main.models.compound_models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="compound",
            name="inchi_key",
        ),
        migrations.AddField(
            model_name="collection",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created Time",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="compound",
            name="inchi",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="compound",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.project",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="structure_available",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="collection",
            name="metadata",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name="compoundoccurrence",
            name="compound",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.compound"
            ),
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dn_id", models.CharField(max_length=11)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "ground_state_file",
                    models.FileField(
                        upload_to=basechem.main.models.compound_models.series_files_path
                    ),
                ),
                (
                    "bound_state_file",
                    models.FileField(
                        upload_to=basechem.main.models.compound_models.series_files_path
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("smiles", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.project",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="compound",
            name="series",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="main.series"
            ),
        ),
    ]
