# Generated by Django 5.1.6 on 2025-02-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0013_rename_expiry_date_member_expeiry_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='expeiry_date',
            new_name='expiry_date',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_Full_Name',
            new_name='member_full_name',
        ),
        migrations.AddField(
            model_name='member',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, to='lms_app.book'),
        ),
    ]
