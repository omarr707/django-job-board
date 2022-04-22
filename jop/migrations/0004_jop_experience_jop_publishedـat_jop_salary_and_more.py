# Generated by Django 4.0.4 on 2022-04-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0003_jop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jop',
            name='publishedـat',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jop',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jop',
            name='vacancv',
            field=models.IntegerField(default=1),
        ),
    ]
