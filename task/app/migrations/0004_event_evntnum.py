# Generated by Django 5.1.3 on 2024-12-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evntNum',
            field=models.IntegerField(default=True),
        ),
    ]