# Generated by Django 2.0.7 on 2018-07-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_doors_all_members'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doorpermissions',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='doorpermissions',
            name='door',
        ),
        migrations.RemoveField(
            model_name='doorpermissions',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='door_access',
            field=models.ManyToManyField(blank=True, null=True, to='portal.Doors'),
        ),
        migrations.DeleteModel(
            name='DoorPermissions',
        ),
    ]
