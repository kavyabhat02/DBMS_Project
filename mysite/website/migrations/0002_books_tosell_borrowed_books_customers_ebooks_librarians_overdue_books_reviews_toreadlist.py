# Generated by Django 2.2.12 on 2022-04-10 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('contact', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='librarians',
            fields=[
                ('librarian_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('contact', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='toReadList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listName', models.TextField()),
                ('customer_id', models.ForeignKey(on_delete='cascade', to='website.customers')),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listName', models.TextField()),
                ('rating', models.IntegerField()),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
            ],
        ),
        migrations.CreateModel(
            name='overdue_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete='cascade', to='website.customers')),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
                ('librarian_id', models.ForeignKey(on_delete='cascade', to='website.librarians')),
            ],
        ),
        migrations.CreateModel(
            name='ebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('hyperlink', models.TextField()),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
            ],
        ),
        migrations.CreateModel(
            name='borrowed_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField()),
                ('customer_id', models.IntegerField()),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
            ],
        ),
        migrations.CreateModel(
            name='books_toSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('price', models.IntegerField()),
                ('isbn', models.ForeignKey(on_delete='cascade', to='website.books_details')),
            ],
        ),
    ]
