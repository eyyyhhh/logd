# Generated by Django 4.2.5 on 2023-10-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
