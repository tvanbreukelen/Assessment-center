# Generated by Django 3.0.4 on 2020-04-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Onderdeel',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='Antwoord',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Reeks',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
