import datetime
from django.db import models

class Course(models.Model):
    MODE_CHOICES = (
        ('LU', 'LU'),
        ('PR', 'PR'),
        ('UE', 'UE'),
        ('VO', 'VO'),
        ('VU', 'VU'),
    )
    courseNr = models.CharField(max_length=7)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=5)
    mode = models.CharField(max_length=2, choices=MODE_CHOICES, blank=True)
    ects = models.FloatField(null=True, blank=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-semester', 'name']

    def __unicode__(self):
        fields = [self.name, self.semester]
        return ' | '.join(fields)

class Assignment(models.Model):
    course = models.ForeignKey(Course)
    due_date = models.DateTimeField(blank=True, null=True)
    pts = models.PositiveSmallIntegerField(null=True, blank=True)
    pts_max = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['due_date']

    def __unicode__(self):
        date = datetime.datetime.strftime(self.date, '%m/%d %H:%M')
        fields = [date, str(self.course)]
        return ' | '.join(fields)

class Lecture(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        date = datetime.datetime.strftime(self.date, '%m/%d %H:%M')
        fields = [date, str(self.course)]
        return ' | '.join(fields)

class Test(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateTimeField(blank=True, null=True)
    pts = models.PositiveSmallIntegerField(blank=True, null=True)
    pts_max = models.PositiveSmallIntegerField(blank=True, null=True)
    grade = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        date = datetime.datetime.strftime(self.date, '%m/%d %H:%M')
        fields = [date, str(self.course)]
        return ' | '.join(fields)
