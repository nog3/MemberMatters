# Generated by Django 2.0.7 on 2018-07-16 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20180716_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cause1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cause1', to='portal.Causes', verbose_name='Cause 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cause2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cause2', to='portal.Causes', verbose_name='Cause 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cause3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cause3', to='portal.Causes', verbose_name='Cause 3'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rfid',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='RFID Tag'),
        ),
    ]
