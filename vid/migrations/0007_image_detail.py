# Generated by Django 3.0.6 on 2020-09-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0006_auto_20200930_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
