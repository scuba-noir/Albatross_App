# Generated by Django 4.1.2 on 2023-02-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albatross_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformrecords',
            name='message',
            field=models.CharField(default='', max_length=250),
        ),
    ]
