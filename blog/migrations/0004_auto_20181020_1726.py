# Generated by Django 2.1.2 on 2018-10-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181020_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
