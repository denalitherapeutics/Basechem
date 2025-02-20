# Generated by Django 3.2.7 on 2022-10-19 16:15

from django.db import migrations, models

import basechem.main.models.collection_models
import basechem.mni_common.storage


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_clear_confgen_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="sdf_file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=basechem.mni_common.storage.select_media_storage,
                upload_to=basechem.main.models.collection_models.collection_files_path,
            ),
        ),
    ]
