# Generated by Django 4.1.7 on 2023-03-16 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle', models.CharField(choices=[('QU', 'Quadriceps'), ('HA', 'Hamstrings'), ('SH', 'Shoulders'), ('FO', 'Forearms'), ('GL', 'Gluteus'), ('BA', 'Back'), ('CH', 'Chest'), ('CA', 'Calves'), ('TR', 'Triceps'), ('BI', 'Biceps'), ('AB', 'Abdominal'), ('NA', 'Not Specified')], default='NA', max_length=2)),
                ('timestamp', models.DateTimeField()),
                ('repetitions', models.IntegerField()),
                ('exertion_value', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.device')),
            ],
        ),
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_count', models.IntegerField()),
                ('value', models.FloatField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.exercise')),
            ],
        ),
    ]
