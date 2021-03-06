# Generated by Django 3.0.6 on 2020-06-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200607_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='id_crew_member_1',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='id_crew_member_2',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='id_crew_member_3',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='id_flight',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='id_helicopter',
        ),
        migrations.AddField(
            model_name='crew_member',
            name='id_flight',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.flight_information'),
        ),
        migrations.AddField(
            model_name='flight_information',
            name='id_helicopter',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.helicopter'),
        ),
    ]
