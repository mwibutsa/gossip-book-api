# Generated by Django 3.0.7 on 2020-07-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_basevotesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='basegossipquestionmodel',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]