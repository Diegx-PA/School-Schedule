import calendar
from datetime import datetime
import webbrowser

subjects = {'monday' : ['AJ','CHE','Free','Free','ETV','CVCJ'],
                'tuesday' : ['Free','D','Free','M','Free','CJ'],
                'wednesday' : ['FY','ZE','Free','CJ','Free','CVM'],
                'thursday' : ['Free','Free','Free','M','AJ','OV'],
                'friday' : ['M','NJ','Free','CJ','PC'],
              }
classes = { 'M':	'https://meet.google.com/lookup/he3ke6bbrg',
            'AJ' : 'https://meet.google.com/lookup/ezbif7rlyx',
            'FY' : 'https://meet.google.com/lookup/elm2azzwhr',
            'ETV' : 'https://meet.google.com/lookup/crxbmkhi43',
            'NJ' : 'https://meet.google.com/lookup/d7fpxkydyg',
            'OV' : 'https://meet.google.com/lookup/b3w74maflb',
            'ZE' : 'https://meet.google.com/lookup/flds5gjt3m',
            'CJ' : 'https://meet.google.com/lookup/hw7pxhpgv3',
            'PR' : 'https://meet.google.com/lookup/cvss3c4igq',
            'CVCJ': 'https://meet.google.com/lookup/egski2zwj6',
            'CVM': 'https://meet.google.com/lookup/hfp5sov7cc',
            'CHE': 'https://meet.google.com/lookup/anc45r5xnt',
            'D': 'https://meet.google.com/lookup/doz7zc6e5w'

          }

def find_day():
    date_and_time = datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[date]
    return day.lower()

def find_classes():
    subs = []
    day = find_day()
    classes = subjects[day]
    if day != 'saturday' and day != 'sunday':
        timings = ['08:00 am - 08:45 am','08:55 am - 09:40 am', '10:00 am - 10:45 am', '10:50 am -  11:40 am', '11:50 am - 12:35 pm', '12:45 pm - 13:30 pm']
        for i in range(6):
            formatted = f'{timings[i]} {classes[i]}'#.format(,)
            subs.append(formatted)
    #if day == 'saturday':
    #    timings = ['09:15 am - 10:15 am','10:30 am - 11:30 am', '11:45 am - 12:45 pm', '12:45 pm - 14:00 pm', '14:00 pm - 17:30 pm']
    #    for i in range(5):
    #        formatted = '{} {}'.format(timings[i],classes[i])
    #        subs.append(formatted)
    #if day == 'sunday':
    #    timings = ['07:30 am - 10:30 am', '10:45 am - 13:45 pm', '14:15 pm', '14:15 pm - 17:15 pm']
    #    for i in range(4):
    #        formatted = '{} {}'.format(timings[i],classes[i])
    #        subs.append(formatted)
    return subs

def classes_today():
    subs = find_classes()
    for i in subs:
        time = datetime.now().time()
        time = str(time).split(":")
        if time[0] == i[0:2] and time[1] >= i[3:5]:
            print('\n' + '\t' + i,' <-- Present Session')
        elif time[0] == i[11:13] and time[1] < i[14:16]:
            print('\n' + '\t' + i,' <-- Present Session')
        else:
            print('\n' + '\t' + i)

def help_menu():
    print('\n' + '\t' + 'class [-a or automate] To automate')
    print('\n' + '\t' + 'class [-h or help] To see this menu')
    print('\n' + '\t' + 'class [subject_name] To open subject_name\'s link')
    print('\n' + '\t' + 'class [-t or today] To see today\'s classes')

def open_link(url):
    webbrowser.open(url)
    print('opened requested page')