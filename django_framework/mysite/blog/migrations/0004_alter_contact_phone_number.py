# Generated by Django 4.2 on 2023-04-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.IntegerField(),
        ),
    ]
