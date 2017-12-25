# Generated by Django 2.0 on 2017-12-25 04:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20171224_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 12, 25, 4, 32, 16, 864156, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='source',
            name='last_sync',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 25, 4, 32, 2, 983935)),
        ),
    ]
