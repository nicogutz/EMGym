# Generated by Django 4.1.7 on 2023-03-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_exercise_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="exercise",
            name="muscle",
            field=models.CharField(
                choices=[
                    ("QUADRICEPS", "Quadriceps"),
                    ("HAMSTRINGS", "Hamstrings"),
                    ("SHOULDERS", "Shoulders"),
                    ("ABDOMINAL", "Abdominal"),
                    ("FOREARMS", "Forearms"),
                    ("GLUTEUS", "Gluteus"),
                    ("BACK", "Back"),
                    ("CHEST", "Chest"),
                    ("CALVES", "Calves"),
                    ("TRICEPS", "Triceps"),
                    ("BICEPS", "Biceps"),
                    ("NA", "Not Specified"),
                ],
                default="NA",
                max_length=15,
            ),
        ),
    ]
