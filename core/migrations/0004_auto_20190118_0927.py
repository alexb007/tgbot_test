# Generated by Django 2.1.5 on 2019-01-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190118_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='current_rate',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Current Rate'),
        ),
    ]
