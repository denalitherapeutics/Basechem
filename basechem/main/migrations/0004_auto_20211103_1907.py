# Generated by Django 3.2.7 on 2021-11-03 23:07

from django.db import migrations, models

import basechem.main.models.compound_models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_series_smiles"),
    ]

    operations = [
        migrations.AddField(
            model_name="compound",
            name="sdf_file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=basechem.main.models.compound_models.select_media_storage,
                upload_to=basechem.main.models.compound_models.compound_files_path,
            ),
        ),
        migrations.AlterField(
            model_name="compound",
            name="epik_file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=basechem.main.models.compound_models.select_media_storage,
                upload_to=basechem.main.models.compound_models.compound_files_path,
            ),
        ),
        migrations.AlterField(
            model_name="compound",
            name="ligprep_file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=basechem.main.models.compound_models.select_media_storage,
                upload_to=basechem.main.models.compound_models.compound_files_path,
            ),
        ),
        migrations.AlterField(
            model_name="series",
            name="bound_state_file",
            field=models.FileField(
                storage=basechem.main.models.compound_models.select_media_storage,
                upload_to=basechem.main.models.compound_models.series_files_path,
            ),
        ),
        migrations.AlterField(
            model_name="series",
            name="ground_state_file",
            field=models.FileField(
                storage=basechem.main.models.compound_models.select_media_storage,
                upload_to=basechem.main.models.compound_models.series_files_path,
            ),
        ),
    ]
