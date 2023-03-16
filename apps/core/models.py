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
        QUADRICEPS = 'QU', _('Quadriceps')
        HAMSTRINGS = 'HA', _('Hamstrings')
        SHOULDERS = 'SH', _('Shoulders')
        FOREARMS = 'FO', _('Forearms')
        GLUTEUS = 'GL', _('Gluteus')
        BACK = 'BA', _('Back')
        CHEST = 'CH', _('Chest')
        CALVES = 'CA', _('Calves')
        TRICEPS = 'TR', _('Triceps')
        BICEPS = 'BI', _('Biceps')
        ABDOMINAL = 'AB', _('Abdominal')
        NA = 'NA', _('Not Specified')

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    muscle = models.CharField(max_length=2, choices=ExerciseType.choices, default=ExerciseType.NA)
    timestamp = models.DateTimeField()
    repetitions = models.IntegerField()
    exertion_value = models.FloatField()


class Datum(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    data_count = models.IntegerField()
    value = models.FloatField()
