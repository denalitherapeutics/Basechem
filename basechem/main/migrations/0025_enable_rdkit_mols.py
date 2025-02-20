# Generated by Django 3.2.7 on 2023-09-13 22:49

import django.contrib.postgres.indexes
from django.db import migrations

import basechem.main.db_utils
from basechem.main.db_utils import RDKitExtension


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_update_gem_ids"),
    ]

    operations = [
        RDKitExtension(),
        migrations.AddField(
            model_name="compound",
            name="rdkit_mol",
            field=basechem.main.db_utils.MolField(
                blank=True, help_text="Field to manage RDKit Mol Objects", null=True
            ),
        ),
        migrations.AddIndex(
            model_name="compound",
            index=django.contrib.postgres.indexes.GistIndex(
                fields=["rdkit_mol"], name="main_compou_rdkit_m_d93a35_gist"
            ),
        ),
    ]
