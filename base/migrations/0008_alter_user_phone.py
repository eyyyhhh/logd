# Generated by Django 4.2.5 on 2023-09-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]