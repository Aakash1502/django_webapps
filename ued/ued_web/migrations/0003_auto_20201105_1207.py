# Generated by Django 3.0.8 on 2020-11-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ued_web', '0002_auto_20201105_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uxwork',
            name='ux_image',
            field=models.ImageField(default='', upload_to='static/home'),
        ),
    ]
