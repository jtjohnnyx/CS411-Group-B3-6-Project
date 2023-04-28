# Generated by Django 4.2 on 2023-04-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0013_teamcache_losses_teamcache_wins'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcache',
            name='pts',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teamcache',
            name='losses',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teamcache',
            name='wins',
            field=models.CharField(max_length=10),
        ),
    ]
