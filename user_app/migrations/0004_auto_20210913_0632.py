# Generated by Django 2.2.12 on 2021-09-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20210912_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionslist',
            name='questionid',
            field=models.IntegerField(),
        ),
    ]
