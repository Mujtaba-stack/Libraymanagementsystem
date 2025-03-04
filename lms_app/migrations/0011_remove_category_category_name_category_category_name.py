# Generated by Django 5.1.6 on 2025-02-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0010_rename_expeiry_date_member_expiry_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Sci-Fic', 'Sci-Fic')], default='Fiction', max_length=220),
        ),
    ]
