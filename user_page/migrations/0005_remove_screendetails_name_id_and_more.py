# Generated by Django 4.0.3 on 2022-03-24 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0004_screendetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screendetails',
            name='name_id',
        ),
        migrations.RemoveField(
            model_name='screendetails',
            name='showings',
        ),
        migrations.RemoveField(
            model_name='showingdetails',
            name='name',
        ),
    ]