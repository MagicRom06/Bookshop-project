# Generated by Django 3.0.7 on 2020-06-25 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='prince',
            new_name='price',
        ),
    ]
