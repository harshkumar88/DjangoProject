# Generated by Django 4.2.2 on 2023-09-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]
