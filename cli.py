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
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from agenda.models import Course, Lecture

# precon: a valid course_id and a date in the form of '%Y/%m/%d %H:%M'
# postcon: adds an assignment for every date provided
def add_assassignments(course_id, dates):
    # select the course
    course = Course.objects.get(pk=course_id)
    # convert the date strings into datetime objects
    convert = lambda s: datetime.datetime.strptime(s, '%Y/%m/%d %H:%M')
    dates = [convert(date) for date in dates]
    # create Assignments and save to the database
    for date in dates:
        l = Assignment(course=course, date=date)
        l.save()

# precon: a valid course_id and a date in the form of '%Y/%m/%d %H:%M'
# postcon: adds a lecture for every date provided
def add_lectures(course_id, dates):
    # select the course
    course = Course.objects.get(pk=course_id)
    # convert the date strings into datetime objects
    convert = lambda s: datetime.datetime.strptime(s, '%Y/%m/%d %H:%M')
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

    if args.add == 'course':
        print('add course...')
    elif args.add == 'lecture':
        print('add lecture...')
    if args.show:
        print('Courses:')
        print_courses()
        print('\nLectures:')
        print_lectures()
    else:
        parser.print_help()

    #add_lectures(3, ['2013/01/03 08:00','2013/02/03 08:00','2013/03/03 08:00'])

if __name__ == '__main__':
    main()
