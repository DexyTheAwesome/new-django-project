# Generated by Django 3.2 on 2021-04-29 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydjangoblog', '0005_auto_20210429_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
