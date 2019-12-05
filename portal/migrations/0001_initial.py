# Generated by Django 2.0.6 on 2019-11-23 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('biography', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('specialty', models.CharField(blank=True, max_length=20)),
                ('level', models.CharField(default='Newbie', max_length=50, null=True)),
                ('current_exp', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
