# Generated by Django 4.2.4 on 2023-08-22 17:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_rename_modelo_veiculo_modelor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="veiculo",
            old_name="modelor",
            new_name="modelo",
        ),
    ]
