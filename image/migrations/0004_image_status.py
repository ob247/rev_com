# Generated by Django 3.0.3 on 2020-07-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_viewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
