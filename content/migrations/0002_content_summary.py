# Generated by Django 2.0 on 2017-12-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='summary',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]