# Generated by Django 4.0.6 on 2022-08-06 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.page')),
            ],
            bases=('core.page',),
        ),
    ]
