# Generated by Django 3.2.13 on 2022-05-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='pics', upload_to='pics'),
            preserve_default=False,
        ),
    ]