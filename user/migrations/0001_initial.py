# Generated by Django 3.2.5 on 2022-07-07 23:01

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30, validators=[user.validators.validate_name])),
                ('nickname', models.CharField(max_length=30)),
            ],
        ),
    ]
