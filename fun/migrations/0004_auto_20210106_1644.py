# Generated by Django 3.1.4 on 2021-01-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0003_auto_20210106_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='slug',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]