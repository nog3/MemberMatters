# Generated by Django 2.0.6 on 2018-07-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20180702_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rfid',
            field=models.CharField(default=1234, max_length=20, verbose_name='RFID Tag'),
            preserve_default=False,
        ),
    ]