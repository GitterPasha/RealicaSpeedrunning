# Generated by Django 4.2 on 2023-06-05 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_rename_accuracy_member_top_accuracy_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='top_time',
            new_name='top_score',
        ),
    ]
