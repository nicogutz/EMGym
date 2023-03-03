from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Device(models.Model):
    uid = models.CharField(max_length=10)


class Exercise(models.Model):
    class ExerciseType(models.TextChoices):
        QUADRICEPS = 'QU', _('QUADRICEPS')
        HAMSTRINGS = 'HA', _('HAMSTRINGS')
        SHOULDERS = 'SH', _('SHOULDERS')
        FOREARMS = 'FO', _('FOREARMS')
        GLUTEUS = 'GL', _('GLUTEUS')
        BACK = 'BA', _('BACK')
        CHEST = 'CH', _('CHEST')
        CALVES = 'CA', _('CALVES')
        TRICEPS = 'TR', _('TRICEPS')
        BICEPS = 'BI', _('BICEPS')
        ABS = 'AB', _('ABS')
        NA = 'NA', _('NOT SPECIFIED')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    muscle = models.CharField(max_length=2, choices=ExerciseType.choices, default=ExerciseType.NA)
    repetitions = models.IntegerField()
    exertion_value = models.FloatField()


class Datum(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    value = models.FloatField()
