



# Generated by Django 5.1.6 on 2025-04-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0009_alter_subtopics_last_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopics',
            name='last_seen',
            field=models.DateTimeField(verbose_name='2025-04-02'),
        ),
    ]
