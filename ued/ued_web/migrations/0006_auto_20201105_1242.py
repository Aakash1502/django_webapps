# Generated by Django 3.0.8 on 2020-11-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ued_web', '0005_auto_20201105_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='art_image',
            field=models.ImageField(default='', upload_to='../images'),
        ),
        migrations.AlterField(
            model_name='uxwork',
            name='ux_image',
            field=models.ImageField(default='', upload_to='../images'),
        ),
    ]
