
import microbit
from microbit import *

def UpdateDisplay():
    display.clear()
    if displayType == 'digital':
        hours, mins = str(time[0]), str(time[1])
        if len(hours) == 1:
            hours = '0' + hours
        if len(mins) == 1:
            mins = '0' + mins
        display.scroll( '{}:{} '.format(hours, mins), delay=150, wait=False, loop=True, monospace=False)
    elif displayType == 'analogue':
        hours, mins = time[0], time[1]
        #hours
        
        if hours >= 12:
            hours = hours - 12
        for pair in analogueDict[hours]:
            display.set_pixel(pair[0], pair[1], 6)

        #mins
        
        analogueDictEntry = 0
        if mins >= 2.5 and mins < 7.5:
            analogueDictEntry = 1
        elif mins >= 7.5 and mins < 12.5:
            analogueDictEntry = 2
        elif mins >= 12.5 and mins < 17.5:
            analogueDictEntry = 3
        elif mins >= 17.5 and mins < 22.5:
            analogueDictEntry = 4
        elif mins >= 22.5 and mins < 27.5:
            analogueDictEntry = 5
        elif mins >= 27.5 and mins < 32.5:
            analogueDictEntry = 6
        elif mins >= 32.5 and mins < 37.5:
            analogueDictEntry = 7
        elif mins >= 37.5 and mins < 42.5:
            analogueDictEntry = 8
        elif mins >= 42.5 and mins < 47.5:
            analogueDictEntry = 9
        elif mins >= 47.5 and mins < 52.5:
            analogueDictEntry = 10
        elif mins >= 52.5 and mins < 57.5:
            analogueDictEntry = 11
        
        for pair in analogueDict[analogueDictEntry]:
            if display.get_pixel(pair[0], pair[1]) == 6:
                overlappingHands.append(pair)
            display.set_pixel(pair[0], pair[1], 8)

def IncrementTime():
    time[1]+=1
    if time[1] >= 60:
        time[1] = 00
        time[0]+=1
        if time[0] >= 24:
            time[0] = 00

if __name__ == '__main__':
    displayType = 'analogue'
    time = [01,15]
    overlappingHands = []
    analogueDict = {
        0 : ((2,2), (2,1), (2,0)),
        1 : ((2,2), (3,1), (3,0)),
        2 : ((2,2), (3,1), (4,1)),
        3 : ((2,2), (3,2), (4,2)),
        4 : ((2,2), (3,3), (4,3)),
        5 : ((2,2), (3,3), (3,4)),
        6 : ((2,2), (2,3), (2,4)),
        7 : ((2,2), (1,3), (1,4)),
        8 : ((2,2), (1,3), (0,3)),
        9 : ((2,2), (1,2), (0,2)),
        10 : ((2,2), (1,1), (0,1)),
        11 : ((2,2), (1,1), (1,0))
        }
    UpdateDisplay()
    nextUpdateTime = microbit.running_time()+60000
    nextOverHandsUpdateTime = microbit.running_time()+1000

    while True:
        if microbit.running_time() >= nextUpdateTime:
            nextUpdateTime = microbit.running_time()+60000
            IncrementTime()
            overlappingHands = []
            UpdateDisplay()
        if running_time() >= nextOverHandsUpdateTime:
            nextOverHandsUpdateTime = running_time()+1000
            for pair in overlappingHands:
                if display.get_pixel(pair[0], pair[1]) == 6:
                    display.set_pixel(pair[0], pair[1], 8)
                else:
                    display.set_pixel(pair[0], pair[1], 6)
        if button_a.was_pressed():
            if displayType == 'digital':
                displayType = 'analogue'
            else:
                displayType = 'digital'
            UpdateDisplay()
            
