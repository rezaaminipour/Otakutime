# Generated by Django 3.1.7 on 2021-04-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20210411_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='background_image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]