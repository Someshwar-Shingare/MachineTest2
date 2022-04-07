# Generated by Django 4.0.3 on 2022-04-07 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=32)),
                ('book_description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=30)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.book')),
            ],
        ),
    ]
