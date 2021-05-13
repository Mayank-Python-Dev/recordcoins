# Generated by Django 3.1.7 on 2021-05-12 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainproject', '0004_usercontent_userfollow'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontent',
            name='FollowerID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='FollowerID', to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfollow',
            name='Followerid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Followerid', to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercontent',
            name='Userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollow',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserID', to=settings.AUTH_USER_MODEL),
        ),
    ]