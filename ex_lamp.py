#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pyIntelligentCity
from time import sleep
   
city = pyIntelligentCity.pyIntelligentCity('COM5')
city.info()

# sprawdzam czy latarnia uliczna jest podłączona
try:
    x = city.lamp_off()
    if x == 4:
        print u'Latarnia uliczna nie jest podłączona'
    else: 
        print u'Latarnię uliczną podłączono do portu: ', x
        # latarnia świeci w trybie ekonomicznym
        print u'Włączenie latarni ulicznej w trybie ekonomicznym - 5 s'
        city.lamp_eco_on()
        sleep(5)
        # latarnia świeci pełną mocą
        print u'Włączenie latarni ulicznej z pełną mocą - 5 s'
        city.lamp_on()
        sleep(5)
        # latarnia jest wyłączona
        print u'Wyłączenie latarni ulicznej - 5 s'
        city.lamp_off()
        sleep(5)
        print u'Automatyczne sterowanie latarnią'
        print u'Sprawdzanie natężenia światła w otoczeniu co sekundę'
        print u'Zakończenie CTRL + C'
        while True:
            if city.isDark():
                city.lamp_eco_on()
                print u'Jest ciemno - latarnia włączona'
            else:
                city.lamp_off()
                print u'Nie jest ciemno - latarnia wyłączona'
            sleep(1)
            
except KeyboardInterrupt:
    print 'Koniec pracy'
    city.lamp_off()
    city.close()


