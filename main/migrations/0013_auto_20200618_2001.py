# Generated by Django 3.0.3 on 2020-06-18 19:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200616_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, unique=True),
        ),
    ]