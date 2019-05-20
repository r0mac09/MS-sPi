import board
import mailing
import gui
import recognizer

gui.GUI() # init gui
recog = recognizer.Recognizer()
try:
    recognized = recog.start()
    while recognized == True or recognized == False:
        if recognized:
            board.unlock()
        else:
            log('Unknown at front door!')
        recognized = recog.start()
except KeyboardInterrupt:
    log('Killed')