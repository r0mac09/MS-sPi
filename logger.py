from datetime import datetime



def init_log():
    logfile = open('log.txt', 'w')
    logfile.write('<%s> Logfile cleared\n' % datetime.now())

def log(logmessage):
    logfile = open('log.txt', 'a+')
    logfile.write('<%s> %s\n' % (datetime.now(), logmessage))
    print(logmessage)