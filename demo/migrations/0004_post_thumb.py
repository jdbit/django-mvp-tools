# Generated by Django 4.0.6 on 2022-08-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]