# Generated by Django 4.1.7 on 2023-03-31 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_acessório_cor_veículo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'Cores'},
        ),
    ]
