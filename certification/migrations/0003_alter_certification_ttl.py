# Generated by Django 3.2.5 on 2022-07-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0002_alter_certification_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='ttl',
            field=models.IntegerField(default=298310757120000000),
        ),
    ]
