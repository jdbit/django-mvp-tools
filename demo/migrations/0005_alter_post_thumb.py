# Generated by Django 4.0.6 on 2022-08-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default-thumb.jpg', null=True, upload_to=''),
        ),
    ]
