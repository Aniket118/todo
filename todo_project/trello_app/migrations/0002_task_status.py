# Generated by Django 2.2.12 on 2021-03-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'PENDING'), ('C', 'COMPLETED'), ('IP', 'IN_PROGRESS'), ('D', 'DROPPED')], default=('IP', 'IN_PROGRESS'), max_length=2),
        ),
    ]
