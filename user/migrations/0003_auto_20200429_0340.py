# Generated by Django 3.0.5 on 2020-04-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200429_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='', max_length=15, null=True, unique=True),
        ),
    ]