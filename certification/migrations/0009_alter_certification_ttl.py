# Generated by Django 3.2.5 on 2022-07-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0008_alter_certification_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='ttl',
            field=models.IntegerField(default=298321261920000000),
        ),
    ]
