# Generated by Django 4.2.2 on 2023-07-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_login',
            name='user_type',
            field=models.CharField(max_length=30),
        ),
    ]
