# Generated by Django 4.0.2 on 2022-08-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_register_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer_applications',
            name='unit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
