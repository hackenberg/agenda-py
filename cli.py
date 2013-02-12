#!/usr/bin/env python2
#
# Python 2.7
#
# requires the DJANGO_SETTINGS_MODULE environment variable to be set
# the main() method sets it automatically to a hardcoded variable
#

import argparse
import datetime
import os

if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from agenda.models import Assignment, Course, Lecture, Test
from django.utils import timezone

DATE_FORMAT = '%d/%m/%Y $H:%M'


def add_course():
    courseNr = input('courseNr (xxx.xxx): ')
    name = input('name: ')
    semester = input('semester ([0-9]{4}[SW]): ')
    add_course(courseNr, name, semester)


def add_course(courseNr, name, semseter):
    c = Course(courseNr=courseNr, name=name, semseter=semseter)
    c.save()

# precon: a valid course_id and a date in the form of DATE_FORMAT
# postcon: adds an assignment for every date provided
def add_assignments(course_id, dates):
    # select the course
    course = Course.objects.get(pk=course_id)
    # convert the date strings into datetime objects
    convert = lambda s: datetime.datetime.strptime(s, DATE_FORMAT)
    dates = [convert(date) for date in dates]
    # create Assignments and save to the database
    for date in dates:
        l = Assignment(course=course, date=date)
        l.save()

# precon: a valid course_id and a date in the form of DATE_FORMAT
# postcon: adds a lecture for every date provided
def add_lectures(course_id, dates):
    # select the course
    course = Course.objects.get(pk=course_id)
    # convert the date strings into datetime objects
    convert = lambda s: datetime.datetime.strptime(s, DATE_FORMAT)
    dates = [convert(date) for date in dates]
    # create Lectures and save to the database
    for date in dates:
        l = Lecture(course=course, date=date)
        l.save()

# precon: a valid course_id and a date in the form of DATE_FORMAT
# postcon: adds a test for every date provided
def add_tests(course_id, dates):
    # select the course
    course = Course.objects.get(pk=course_id)
    # convert the date strings into datetime objects
    convert = lambda s: datetime.datetime.strptime(s, DATE_FORMAT)
    dates = [convert(date) for date in dates]
    # create Lectures and save to the database
    for date in dates:
        l = Test(course=course, date=date)
        l.save()


def print_courses():
    for c in Course.objects.all():
        print(str(c.id) + ' | ' + str(c))
        print(c.get_url())


def print_lectures(course=None):
    if course == None:
        lectures = Lecture.objects.all()
    else:
        courses = Course.objects.get(name=course)
        lectures = Lecture.objects.filter(course=course)
    for l in lectures:
        print(str(l.id) + ' | ' + str(l))


def get_upcoming_events(days):
    isUpcoming = lambda e: timezone.now() <= e.date <= timezone.now() + datetime.timedelta(days=days)
    assignments = [e for e in Assignment.objects.all() if isUpcoming(e)]
    lectures = [e for e in Lecture.objects.all() if isUpcoming(e)]
    tests = [e for e in Test.objects.all() if isUpcoming(e)]
    events = assignments + lectures + tests
    for e in events:
        print(str(e.id) + ' | ' + str(e))
    return events


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add',
                        help='add an event of the specified type \
                              (course | lecture) to the database')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='prompts you for every required field')
    parser.add_argument('-s', '--show', action='store_true',
                        help='print stuff from the database')
    parser.add_argument('-u', '--upcoming', dest='days', type=int,
                        help='show events in the next n days')
    args = parser.parse_args()

    if args.show:
        print('Courses:')
        print_courses()
        print('\nLectures:')
        print_lectures()

    if args.days:
        get_upcoming_events(args.days)

    if args.add == 'course':
        if args.interactive:
            add_course()
        else:
            print('add course...')
    elif args.add == 'lecture':
        print('add lecture...')


if __name__ == '__main__':
    main()
