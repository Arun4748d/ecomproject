# Generated by Django 4.2.2 on 2023-07-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_tb_registration_login_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_registration',
            old_name='login_id',
            new_name='login',
        ),
    ]
