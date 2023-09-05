# Generated by Django 4.2.4 on 2023-09-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='customer_status',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('BRONZE', 'Bronze'), ('SILVER', 'Silver'), ('GOLD', 'GOLD')], default='Normal', max_length=6),
        ),
    ]
