# Generated by Django 3.1.7 on 2021-03-11 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('C', 'COMPLETED'), ('IP', 'IN_PROGRESS'), ('D', 'DROPPED')], default=('IP', 'IN_PROGRESS'), max_length=2)),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello_app.tasklist')),
            ],
        ),
    ]
