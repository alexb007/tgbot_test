# Generated by Django 2.1.5 on 2019-01-18 05:29

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Currency Name')),
                ('current_rate', models.FloatField(verbose_name='Current Rate')),
                ('rate_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='current_rate', verbose_name='Last Rate Update')),
            ],
            options={
                'verbose_name': 'Crypto Currency',
                'verbose_name_plural': 'Crypto Currencies',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Website Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('status', models.CharField(default=None, editable=False, max_length=3, null=True, verbose_name='Website Status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status')),
            ],
            options={
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
    ]
