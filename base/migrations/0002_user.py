# Generated by Django 4.2.5 on 2023-09-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernum', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('usertype', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')])),
            ],
        ),
    ]
