# Generated by Django 4.0 on 2022-05-24 09:39

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.detail


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0014_filmdetails_alter_rating_options_remove_rating_film_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmDetailView',
            fields=[
                ('film_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cinema_app.film')),
            ],
            bases=('cinema_app.film', django.views.generic.detail.DetailView),
        ),
        migrations.RemoveField(
            model_name='search',
            name='filmdetails_ptr',
        ),
        migrations.AddField(
            model_name='film',
            name='url',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='FilmDetails',
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
