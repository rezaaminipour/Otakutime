# Generated by Django 3.1.5 on 2021-04-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_auto_20210414_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]