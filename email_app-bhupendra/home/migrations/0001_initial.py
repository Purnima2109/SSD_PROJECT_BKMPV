# Generated by Django 3.2.9 on 2021-11-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.CharField(max_length=100)),
                ('participant_password', models.CharField(max_length=100)),
                ('participant_email', models.CharField(max_length=100)),
                ('task_id', models.CharField(max_length=100)),
                ('recording_url', models.CharField(max_length=100)),
                ('notes_url', models.CharField(max_length=100)),
            ],
        ),
    ]
