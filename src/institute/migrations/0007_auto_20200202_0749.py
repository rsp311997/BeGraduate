# Generated by Django 3.0.2 on 2020-02-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_auto_20200202_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longititude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
