# Generated by Django 3.0.5 on 2021-05-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='customerMobileNo',
            field=models.CharField(max_length=30),
        ),
    ]
