# Generated by Django 5.1.6 on 2025-02-24 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_name',
            new_name='book_title',
        ),
    ]
