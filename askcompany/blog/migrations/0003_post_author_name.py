# Generated by Django 2.2.9 on 2020-01-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='annoymous', max_length=20),
            preserve_default=False,
        ),
    ]
