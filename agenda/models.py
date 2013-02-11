import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from django.db import models


class Course(models.Model):
    MODE_CHOICES = (
        ('LU', 'LU'),
        ('PR', 'PR'),
        ('UE', 'UE'),
        ('VO', 'VO'),
        ('VU', 'VU'),
    )
    courseNr_validators = [RegexValidator(regex=r'[0-9]{3}\.[A0-9][0-9]{2}')]
    semester_validators = [RegexValidator(regex=r'[0-9]{4][SW]+')]
    grade_validators = [MinValueValidator(1), MaxValueValidator(5)]

    courseNr = models.CharField(max_length=7, validators=courseNr_validators)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=5, validators=semester_validators)
    mode = models.CharField(max_length=2, choices=MODE_CHOICES)
    ects = models.FloatField(null=True, blank=True)
    grade = models.PositiveSmallIntegerField(validators=grade_validators,
                                             blank=True, null=True)

    class Meta:
        ordering = ['-semester', 'name']
        unique_together = ('courseNr', 'semester')

    def __unicode__(self):
        fields = [self.name, self.semester]
        return ' | '.join(fields)


class Event(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateTimeField()

    class Meta:
        abstract = True
        ordering = ['date']
        unique_together = ('course', 'date')

    def __unicode__(self):
        date = datetime.datetime.strftime(self.date, '%d/%m %H:%M')
        fields = [date, str(self.course)]
        return ' | '.join(fields)


class Assignment(Event):
    pts = models.PositiveSmallIntegerField(null=True, blank=True)
    pts_max = models.PositiveSmallIntegerField(null=True, blank=True)


class Lecture(Event):
    location = models.CharField(max_length=64)


class Test(Event):
    grade_validators = [MinValueValidator(1), MaxValueValidator(5)]

    pts = models.PositiveSmallIntegerField(blank=True, null=True)
    pts_max = models.PositiveSmallIntegerField(blank=True, null=True)
    grade = models.PositiveSmallIntegerField(validators=grade_validators,
                                             blank=True, null=True)
