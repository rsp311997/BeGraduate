# Generated by Django 3.0.2 on 2020-02-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20200131_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutemodel',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/college/'),
        ),
    ]
