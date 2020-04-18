# Generated by Django 3.0.2 on 2020-02-07 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_auto_20200207_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GIVEN_REVIEW', to=settings.AUTH_USER_MODEL),
        ),
    ]