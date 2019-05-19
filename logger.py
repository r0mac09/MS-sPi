from datetime import datetime

def log(logmessage):
    logfile = open('log.txt', 'a+')
    logfile.write('<%s> %s\n' % (datetime.now(), logmessage))
    print(logmessage)