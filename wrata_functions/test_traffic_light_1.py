# -*- coding: utf-8 -*-

# Przykład z pojedynczym sygnalizatorem drogowym

# Import modułów programu

import city
import traffic_light
from time import sleep

# Lista dostępnych urządzeń
city.info()

# Wyłączenie sygnalizatora
traffic_light.off()
print u'Test sygnalizatora'
print u'Światło żółte pulsujące - 15 s\n'

# Światło żółte pulsujące 15 s
traffic_light.yellow_blink(15)

try:
    print u'Cykliczna zmiana świateł (Ctrl+C - zakończenie programu)'
    while True:
        # Światło czerwone 5 s
        traffic_light.red_on()
        sleep(5)
        # Światło czerwone i żółte 1.25 s
        traffic_light.yellow_on()
        sleep(1.25);
        traffic_light.red_off()
        traffic_light.yellow_off()
        # Swiatło zielone 5 s
        traffic_light.green_on()
        sleep(5)
        traffic_light.green_off()
        traffic_light.yellow_on()
        sleep(1.25);
        traffic_light.yellow_off()

# Przerwanie pracy programu Ctrl + C
except KeyboardInterrupt:
    traffic_light.off()
    city.close()
