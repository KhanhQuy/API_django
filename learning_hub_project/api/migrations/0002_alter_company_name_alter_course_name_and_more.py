# Generated by Django 4.2.1 on 2023-06-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company", name="name", field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="course", name="name", field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="learninghub",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
