# Generated by Django 3.1.4 on 2020-12-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='p_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('cperson', models.CharField(max_length=100)),
                ('mob', models.BigIntegerField()),
                ('uname', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
