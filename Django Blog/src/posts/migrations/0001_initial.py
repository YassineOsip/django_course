# Generated by Django 3.0.7 on 2020-06-06 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('publishedAt', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
    ]
