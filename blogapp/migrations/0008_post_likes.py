# Generated by Django 3.1.1 on 2021-04-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_post_commentcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]