# Generated by Django 2.2.7 on 2019-11-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20191126_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Location',
            field=models.CharField(default='Karachi', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='Purpose',
            field=models.CharField(default='Karachi', max_length=200),
            preserve_default=False,
        ),
    ]
