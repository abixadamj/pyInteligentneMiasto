#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pyIntelligentCity
from time import sleep
   
city = pyIntelligentCity.pyIntelligentCity('COM5')
city.info()

# sprawdzam czy sygnalizotor drogowy jest podłączony
try:
    x = city.SD_all_off()
    if x == 4:
        print u'Sygnalizator drogowy nie jest podłączony'
    else: 
        print u'Sygnalizator drogowy podłączono do portu: ', x
        # światło żółte pulsujące
        print u'Światło żółte pulsujące - 10 s'
        city.SD_yellow_blink(10)
        # cykl zmiany świateł
        print u'Cykliczna zmiana świateł'
        print u'Zakończenie CTRL + C'
        while True:
            # światło czerwone 3 s
            city.SD_red_on()
            sleep(3)
            # światło czerwone i żółte 1 s
            city.SD_yellow_on()
            sleep(1)
            # światło zielone 3 s
            city.SD_red_off()
            city.SD_yellow_off()
            city.SD_green_on()
            sleep(3)
            # światło żółte 1 s
            city.SD_green_off()
            city.SD_yellow_on()
            sleep(1)
            city.SD_yellow_off()
except KeyboardInterrupt:
    print 'Koniec pracy'
    city.SD_all_off()
    city.close()


