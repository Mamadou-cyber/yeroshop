# Generated by Django 5.2.1 on 2025-06-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
