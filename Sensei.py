import os
import time

Hours = 0
Minutes = 0
Seconds = 0

while(True):
    time.sleep(1)
    Seconds += 1
    if(Seconds >= 60): 
        Minutes += 1
        Seconds = 0
    if(Minutes >= 60):
        Hours += 1
        Minutes = 0
    if(Hours >= 12): Hours = 1

    os.system('clear')
    print(str(Hours)+':'+str(Minutes)+':'+str(Seconds))


for che in range(100):
    print 
  