# Generated by Django 2.1.5 on 2019-01-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190118_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Currency Name'),
        ),
    ]
