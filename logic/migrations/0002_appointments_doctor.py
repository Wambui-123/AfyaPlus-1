# Generated by Django 4.0.5 on 2022-06-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='logic.doctors'),
        ),
    ]
