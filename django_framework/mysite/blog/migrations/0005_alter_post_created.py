# Generated by Django 4.2 on 2023-05-01 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_contact_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
