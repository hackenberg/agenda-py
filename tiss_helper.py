#!/usr/bin/env python2
#
# TODO: verify ssl
#

import os
import requests
from bs4 import BeautifulSoup

if os.environ.get('DJANGO_SETTINGS_MODULE') == None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from agenda.models import Course

AUTH_URL = 'https://iu.zid.tuwien.ac.at/AuthServ.authenticate'
TISS_URL = 'https://tiss.tuwien.ac.at'

UNAME = ''       # TODO: REMOVE ASAP
PWD = '',     # TODO: REMOVE ASAP

def authenticate(username, password):
    auth_payload = {
        'name': username,
        'pw': password,
        'app': 76  # TISS
    }
    session = requests.Session()
    session.post(AUTH_URL, data=auth_payload)
    return session;

def sync():
    session = authenticate(UNAME, PWD)
    response = session.get(TISS_URL + '/education/favorites.xhtml')
    soup = BeautifulSoup(response.text)
    for elem in soup.find_all('td', 'favoritesTitleCol'):
        try:
            courseNr = link.find('span', title='LVA Nr.').contents[0]
            name = link.find('a').contents[0]
            semester = link.find('span', title='Semester').contents[0]
            typ = link.find('span', title='Typ').contents[0]
            course = Course(courseNr=courseNr, name=name, semester=semester,
                            mode=mode)
            course.save()
        except AttributeError:
            pass  # gets thrown when BeautifulSoup encounters the 'summe' <td>
            # maybe TODO: handle the field properly

def main():
    session = authenticate(UNAME, PWD)
    response = session.get(TISS_URL + '/education/favorites.xhtml')
    soup = BeautifulSoup(response.text)
    for link in soup.find_all('td', 'favoritesTitleCol'):
        try:
            courseNr = link.find('span', title='LVA Nr.').contents[0]
            name = link.find('a').contents[0]
            semester = link.find('span', title='Semester').contents[0]
            typ = link.find('span', title='Typ').contents[0]
            href = link.find('a')
            print('name:     ' + name)
            print('courseNr: ' + courseNr)
            print('semester: ' + semester)
            print('typ:      ' + typ.strip(', '))
            print('href:     ' + TISS_URL + href['href'] + '\n')
        except AttributeError:
            pass  # gets thrown when BeautifulSoup encounters the 'summe' <td>
            # maybe TODO: handle the field properly

if __name__ == '__main__':
    main()
