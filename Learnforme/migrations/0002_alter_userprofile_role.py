# Generated by Django 4.1 on 2024-09-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learnforme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=255),
        ),
    ]
