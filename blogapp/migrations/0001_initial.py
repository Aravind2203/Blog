# Generated by Django 3.1.1 on 2021-04-22 15:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('TitleSlug', models.SlugField()),
                ('OverView', models.TextField()),
                ('Content', ckeditor.fields.RichTextField()),
                ('Category', models.ManyToManyField(to='blogapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Comment', models.TextField()),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.post')),
            ],
        ),
    ]