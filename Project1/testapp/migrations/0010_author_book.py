# Generated by Django 4.0.3 on 2022-04-07 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_remove_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='testapp.book'),
        ),
    ]
