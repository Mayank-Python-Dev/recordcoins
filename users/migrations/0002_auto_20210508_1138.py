# Generated by Django 3.1.7 on 2021-05-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='City',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
