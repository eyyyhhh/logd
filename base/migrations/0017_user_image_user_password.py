# Generated by Django 4.2.5 on 2023-10-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_logs_date_alter_logs_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='1', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
