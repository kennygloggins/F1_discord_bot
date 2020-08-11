# By: Kenny_G_Loggins
# Created on: 8/6/20, 1:51 PM
# File: Calender.py
# Project: F1_discord_bot

from __future__ import print_function
import time
import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from config import googcal, webhook, lights_out
# from apscheduler.scheduler import Scheduler
from apscheduler.schedulers.blocking import BlockingScheduler


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

sched = BlockingScheduler()

def calender():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId=googcal, timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events


def cal_clostest_event_info():
    events = calender()
    caldict = {}
    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        caldict[start] = event['summary']
    # time = [x for x in list(caldict)[0:1]]
    return start, caldict[start]

def parse_time():
    sched.remove_job(id='end')
    time, info = cal_clostest_event_info()
    time_tmp = time.split(':')
    minute = time_tmp[1]
    time_tmp = time_tmp[0].split('T')
    hour = time_tmp[1]
    time_tmp = time_tmp[0].split('-')
    year = time_tmp[0]
    month = time_tmp[1]
    day = time_tmp[2]
    # Schedule job to run event on given date
    sched.add_job(event, 'cron', id='tmp', year=year, month=month, day=day, hour=hour, minute=minute, args=info)


# Define the function that is to be executed
def event(info):
    sched.remove_job(id='tmp')
    
    parse_time()

sched.start()
