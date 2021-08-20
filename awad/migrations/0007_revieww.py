# Generated by Django 3.0 on 2021-08-20 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awad', '0006_auto_20210820_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revieww',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('design', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('usability', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('content', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awad.Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
