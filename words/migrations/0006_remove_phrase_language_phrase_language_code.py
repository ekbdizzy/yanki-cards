# Generated by Django 4.0.4 on 2022-07-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_alter_translationsstack_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phrase',
            name='language',
        ),
        migrations.AddField(
            model_name='phrase',
            name='language_code',
            field=models.CharField(choices=[('en', 'english'), ('ru', 'russian'), ('tr', 'turkish')], default='en', max_length=2, verbose_name='Language_code'),
        ),
    ]
