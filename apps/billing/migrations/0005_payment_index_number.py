# Generated by Django 3.2.5 on 2022-05-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20220522_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='index_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
