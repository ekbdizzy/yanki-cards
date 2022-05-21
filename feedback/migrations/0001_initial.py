# Generated by Django 4.0.4 on 2022-05-18 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('problem', 'I have a problem'), ('suggestion', "I'd like to suggest you"), ('thanks', 'I just want to thank you'), ('other', 'other')], max_length=60, verbose_name='Title')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('text', models.TextField(default='', max_length=400, verbose_name='Text')),
                ('status', models.CharField(choices=[('new', 'New'), ('important', 'Important'), ('active', 'Active'), ('closed', 'Closed')], max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited at')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]