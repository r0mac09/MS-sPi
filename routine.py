# import board
import mailing

from datetime import datetime
from logger import log

away_interval = [datetime.now(), datetime.now()]
doNotDisturb = False
awaySet = False

def init():
    log('Routine initialized.')

def away():
    global away_interval
    global doNotDisturb
    global awaySet
    if doNotDisturb:
        return True

    if not awaySet:
        return False
    else:
        now = datetime.now()
        if away_interval[0] < now and away_interval[1] > now:
            return True
        else:
            return False

def setDnd():
    global doNotDisturb
    if not doNotDisturb:
        doNotDisturb = True

def setAwayInterval(start, end):
    global away_interval
    global awaySet
    away_interval = [datetime.strptime(start, '%Y-%m-%d %H:%M'), datetime.strptime(end, '%Y-%m-%d %H:%M')]
    awaySet = True

def setAvailable():
    global away_interval
    global doNotDisturb
    doNotDisturb = False
    away_interval = [datetime.now(), datetime.now()]
