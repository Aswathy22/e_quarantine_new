# Generated by Django 3.1.4 on 2020-12-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0023_u_reg_f_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='u_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='u_reg',
            name='m_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
