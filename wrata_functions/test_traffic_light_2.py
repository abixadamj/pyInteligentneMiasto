# -*- coding: utf-8 -*-

# Przykład z dwoma sygnalizatorami drogowymi (skrzyżowanie)

# Import modułów programu

import city
import traffic_light
import traffic_light2

from time import sleep

# Lista dostępnych urządzeń
city.info()

# Wyłączenie sygnalizatorów
traffic_light.off()
traffic_light2.off()

print 'Test sygnalizatora nr 1'
print ' Światło żółte pulsujące - 5 s\n'
# Światło żółte pulsujące 5 s
traffic_light.yellow_blink(5)
print 'Test sygnalizatora nr 2'
print ' Światło żółte pulsujące - 5 s\n'
# Światło żółte pulsujące 5 s
traffic_light2.yellow_blink(5)

print 'Światło żółte pulsujące na skrzyżowaniu - 10 s'
for i in range(10):
    traffic_light.yellow_on()
    traffic_light2.yellow_on()
    sleep(0.5);
    traffic_light.yellow_off()
    traffic_light2.yellow_off()
    sleep(0.5);
    
try:
    print 'Cykliczna zmiana świateł na skrzyżowaniu (Ctrl+C - zakończenie programu)'
    while True:
        # Światło czerwone / światło zielone - 5 s
        traffic_light.yellow_off()
        traffic_light2.red_off()
        traffic_light2.yellow_off()
        traffic_light.red_on()
        traffic_light2.green_on()
        sleep(5)

        # Światło czerwone i żółte / światło żółte - 1.25 s 
        traffic_light.yellow_on()
        traffic_light2.green_off()
        traffic_light2.yellow_on()
        sleep(1.25);

        # Swiatło zielone / światło czerwone - 5 s
        traffic_light.red_off()
        traffic_light.yellow_off()
        traffic_light2.yellow_off()
        traffic_light.green_on()
        traffic_light2.red_on()
        sleep(5)

        # Światło żółte / światło czerwone i żółte - 1.25 s
        traffic_light.green_off()
        traffic_light.yellow_on()
        traffic_light2.yellow_on()
        sleep(1.25);
        
# Przerwanie pracy programu Ctrl + C
except KeyboardInterrupt:
    traffic_light.off()
    traffic_light2.off()
    city.close()
