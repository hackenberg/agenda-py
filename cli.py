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

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from agenda.models import Assignment, Course, Lecture

DATE_FORMAT = '%d/%m/%Y $H:%M'

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

def print_courses():
    for c in Course.objects.all():
        print(str(c.id) + ' | ' + str(c))

def print_lectures(course=None):
    if course == None:
        lectures = Lecture.objects.all()
    else:
        courses = Course.objects.get(name=course)
        lectures = Lecture.objects.filter(course=course)
    for l in lectures:
        print(str(l.id) + ' | ' + str(l))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( '-a', '--add'
                       , help='add an event of the specified type \
                               (course | lecture) to the database')
    parser.add_argument( '-s', '--show', action='store_true'
                       , help='print stuff from the database')
    args = parser.parse_args()

    if args.show:
        print('Courses:')
        print_courses()
        print('\nLectures:')
        print_lectures()
    elif args.add == 'course':
        print('add course...')
    elif args.add == 'lecture':
        print('add lecture...')
    else:
        parser.print_help()

    #add_lectures(2, ['01/03/2013 08:00','02/03/2013 08:00','03/03/2013 08:00'])

if __name__ == '__main__':
    main()
