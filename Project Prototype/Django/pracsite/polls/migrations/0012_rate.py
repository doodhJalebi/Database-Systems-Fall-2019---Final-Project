# Generated by Django 2.2.7 on 2019-11-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20191126_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
            ],
        ),
    ]
