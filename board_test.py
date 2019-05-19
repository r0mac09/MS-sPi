import board
import time

board.setup()

board.switchYellowOn()

time.sleep(3)

board.switchBlueOn()

time.sleep(3)

board.kill()
