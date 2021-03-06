# Generated by Django 3.1a1 on 2020-06-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_mentorship', '0009_skill_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='can_help',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='help_wanted',
        ),
        migrations.AddField(
            model_name='experience',
            name='exp_type',
            field=models.IntegerField(choices=[(0, 'Want Help'), (1, 'Can Help')], default=0),
            preserve_default=False,
        ),
    ]
