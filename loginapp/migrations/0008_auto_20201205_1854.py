# Generated by Django 3.1.4 on 2020-12-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_auto_20201204_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='pname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='uname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
