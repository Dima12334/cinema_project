# Generated by Django 4.0 on 2022-05-30 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0017_alter_ticket_hall_alter_ticket_purchased_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinemahall', verbose_name='Номер залу'),
        ),
    ]
