# Generated by Django 4.2.5 on 2023-11-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]