# Generated by Django 3.0 on 2021-08-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awad', '0008_auto_20210826_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='images/Blank-Avatar.JPG', null=True, upload_to=''),
        ),
    ]
