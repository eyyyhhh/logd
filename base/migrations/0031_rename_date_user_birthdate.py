# Generated by Django 4.2.5 on 2023-11-20 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_user_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date',
            new_name='birthdate',
        ),
    ]