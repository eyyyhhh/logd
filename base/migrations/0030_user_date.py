# Generated by Django 4.2.5 on 2023-11-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_logs_health_logs_q1_logs_q2_logs_q3_logs_q4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
