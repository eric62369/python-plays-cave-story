import time
from keyboard_input_engine import CONTROLS, SendKeyPress, SendKeyRelease

def first_room():
    SendKeyPress(CONTROLS['LEFT'])
    wait(0.25)
    SendKeyPress(CONTROLS['JUMP'])
    wait(1)
    SendKeyRelease(CONTROLS['LEFT'])
    SendKeyRelease(CONTROLS['JUMP'])

    wait(0.02)
    SendKeyPress(CONTROLS['RIGHT'])
    SendKeyPress(CONTROLS['JUMP'])
    wait(2)
    SendKeyRelease(CONTROLS['RIGHT'])
    SendKeyRelease(CONTROLS['JUMP'])

    wait(0.02)
    SendKeyPress(CONTROLS['LEFT'])
    wait(0.5)
    SendKeyRelease(CONTROLS['LEFT'])

    SendKeyPress(CONTROLS['DOWN'])
    wait(0.02)
    SendKeyRelease(CONTROLS['DOWN'])    

'''
Wait (pause thread) for a given amount of seconds
'''
def wait(seconds):
    time.sleep(seconds)

if (__name__ == '__main__'):
    wait(3)
    first_room()