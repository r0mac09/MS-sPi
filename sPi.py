from recognizer import Recognizer
from logger import init_log
import board

init_log()

board.setup()

recog = Recognizer()
recog.recognize()