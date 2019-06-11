# Generated by Django 2.1.5 on 2019-01-18 07:44

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='200', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='website',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed'),
        ),
    ]
