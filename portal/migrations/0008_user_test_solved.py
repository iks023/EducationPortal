# Generated by Django 3.0 on 2019-12-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20191205_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_test',
            name='solved',
            field=models.BooleanField(null=True),
        ),
    ]
