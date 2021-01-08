# Generated by Django 3.1.4 on 2021-01-06 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=20)),
                ('opponent_name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True)),
                ('your_video', models.FileField(upload_to='')),
                ('opponent_video', models.FileField(upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('your_video_likes', models.IntegerField(default=0)),
                ('opponent_video_likes', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]