# Generated by Django 4.0.2 on 2022-06-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_farm_revenue_revenue_farm_revenue_revenue_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='a',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='b',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='c',
            field=models.IntegerField(default='0'),
        ),
    ]
