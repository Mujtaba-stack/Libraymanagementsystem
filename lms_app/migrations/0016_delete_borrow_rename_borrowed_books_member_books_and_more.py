# Generated by Django 5.1.6 on 2025-03-04 15:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0015_borrow_delete_barrow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Borrow',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='borrowed_books',
            new_name='books',
        ),
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.RemoveField(
            model_name='book',
            name='available_copies',
        ),
        migrations.RemoveField(
            model_name='book',
            name='total_copies',
        ),
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Borrowed', 'Borrowed')], default='Available', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='member',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='member',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
