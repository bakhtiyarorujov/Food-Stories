# Generated by Django 4.2.6 on 2023-10-27 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_comment_story_alter_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='tag',
            new_name='tags',
        ),
    ]