# Generated by Django 4.0 on 2022-07-10 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0026_like_dislike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dislike',
            old_name='review_id',
            new_name='object_id',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='review_id',
            new_name='object_id',
        ),
    ]
