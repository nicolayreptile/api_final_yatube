# Generated by Django 3.0.5 on 2020-04-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200420_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]