# Generated by Django 3.2.5 on 2022-01-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='degree_level',
            new_name='four_index',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='degree_time',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='degree_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='place_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='programme_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='start_year',
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
