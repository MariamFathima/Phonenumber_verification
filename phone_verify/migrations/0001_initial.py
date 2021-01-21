# Generated by Django 3.1.5 on 2021-01-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile_number', models.CharField(max_length=10)),
                ('key', models.CharField(blank=True, max_length=100)),
                ('isVerified', models.BooleanField(default=False)),
            ],
        ),
    ]
