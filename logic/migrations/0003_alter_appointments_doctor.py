# Generated by Django 4.0.5 on 2022-06-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_appointments_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='logic.doctors'),
        ),
    ]
