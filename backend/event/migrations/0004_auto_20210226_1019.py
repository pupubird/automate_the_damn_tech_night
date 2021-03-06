# Generated by Django 3.1.6 on 2021-02-26 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0001_initial'),
        ('event', '0003_auto_20210226_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='event.event'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='speaker.speaker'),
        ),
    ]
