# Generated by Django 3.2 on 2021-05-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydjangoblog', '0007_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
