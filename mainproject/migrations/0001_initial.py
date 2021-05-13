# Generated by Django 3.1.7 on 2021-05-08 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Share_ID', models.IntegerField()),
                ('Share_Name', models.CharField(max_length=100)),
                ('Share_Count', models.IntegerField()),
                ('Share_Price', models.FloatField()),
                ('Status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=50)),
                ('Share_Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seller_ID', models.IntegerField()),
                ('Share_Count', models.IntegerField()),
                ('Date_time', models.DateField(auto_now_add=True)),
                ('Amount', models.IntegerField()),
                ('Share_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainproject.usershare')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
