# Generated by Django 4.2.7 on 2023-11-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userverifycode',
            name='user',
        ),
        migrations.AddField(
            model_name='userverifycode',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
