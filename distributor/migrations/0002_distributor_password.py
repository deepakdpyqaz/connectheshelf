# Generated by Django 3.1.4 on 2020-12-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='password',
            field=models.CharField(default=models.CharField(max_length=15, primary_key=True, serialize=False), max_length=20),
        ),
    ]
