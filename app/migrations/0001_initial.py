# Generated by Django 5.0.4 on 2024-04-21 18:52

import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('password', models.CharField(max_length=10)),
                ('ref_code', models.CharField(default='R3KKbYpk', unique=True)),
            ],
        ),
    ]