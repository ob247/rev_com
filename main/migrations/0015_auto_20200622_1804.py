# Generated by Django 3.0.3 on 2020-06-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_blog_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimumWithdrawAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
            ],
            options={
                'verbose_name_plural': 'Minimum Withdraw Amount',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/uploads'),
        ),
    ]