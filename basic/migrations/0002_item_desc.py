# Generated by Django 3.0.8 on 2021-03-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
