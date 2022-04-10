# Generated by Django 2.2.12 on 2022-04-08 04:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books_details',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('title', models.TextField()),
                ('summary', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
    ]
