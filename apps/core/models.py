from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=10, unique=True)

    def __abs__(self):
        return self.user


class Exercise(models.Model):
    class ExerciseType(models.TextChoices):
        QUADRICEPS = 'QUADRICEPS', _('Quadriceps')
        HAMSTRINGS = 'HAMSTRINGS', _('Hamstrings')
        SHOULDERS = 'SHOULDERS', _('Shoulders')
        ABDOMINAL = 'ABDOMINAL', _('Abdominal')
        FOREARMS = 'FOREARMS', _('Forearms')
        GLUTEUS = 'GLUTEUS', _('Gluteus')
        BACK = 'BACK', _('Back')
        CHEST = 'CHEST', _('Chest')
        CALVES = 'CALVES', _('Calves')
        TRICEPS = 'TRICEPS', _('Triceps')
        BICEPS = 'BICEPS', _('Biceps')
        NA = 'NA', _('Not Specified')

    class Meta:
        unique_together = ['device', 'timestamp']

    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    muscle = models.CharField(max_length=15, choices=ExerciseType.choices, default=ExerciseType.NA)
    timestamp = models.DateTimeField(null=False)
    repetitions = models.IntegerField()
    exertion_value = models.FloatField()


class Datum(models.Model):
    class Meta:
        unique_together = ['exercise', 'data_count']

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    data_count = models.IntegerField()
    value = models.FloatField()
