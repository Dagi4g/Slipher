



# Generated by Django 5.2 on 2025-04-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0015_rename_revison_count_subtopicmemory_revision_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopics',
            name='last_seen',
            field=models.DateTimeField(verbose_name='2025-04-27'),
        ),
    ]
