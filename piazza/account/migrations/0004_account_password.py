# Generated by Django 3.2.6 on 2021-08-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210821_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default='123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
