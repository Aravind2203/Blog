# Generated by Django 3.1.1 on 2021-04-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20210427_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='DateAdded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
