# Generated by Django 5.2 on 2025-06-20 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0020_subtopics_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopicmemory',
            name='last_reviewed',
        ),
    ]
