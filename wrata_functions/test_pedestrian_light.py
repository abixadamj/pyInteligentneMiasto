# -*- coding: utf-8 -*-

# Przykład wykorzystania sygnalizatora na przejściu dla pieszych
# współpracującego z sygnalizatorem drogowym dla samochodów

# Import modułów
import city
import traffic_light
import pedestrian_light
from time import sleep

# Lista urządzeń podłączonych do sterownika
city.info()

# Czerwone światło dla pieszych
pedestrian_light.red_on()
pedestrian_light.green_off()
# Zielone światło dla pojazdów
traffic_light.off()
traffic_light.green_on()

try:
    while True:
        # Sprawdzanie czy pieszy zarządał zmiany światła na zielone
        if pedestrian_light.is_pressed():
            print u'Pieszy na krawężniku'
            # Pieszy nacisnął przycisk - za pół sekundy rozpocznie się zmiana świateł
            sleep(0.5)
            # Żółte światło dla pojazdów 
            traffic_light.yellow_on()
            traffic_light.green_off()
            sleep(0.5)
            # Czerwone światło dla pojazdów
            traffic_light.red_on()
            traffic_light.yellow_off()
            print u'Pojazdy stoją!'
            sleep(0.5)
            # Zielone światło dla pieszego
            pedestrian_light.red_off()
            pedestrian_light.green_on()
            print u'Pieszy przechodzi'
            sleep(3)
            # Pulsujące światło zielone dla pieszego
            pedestrian_light.green_blink() # domyślnie 2 s
            # Czerwone światło dla pieszego
            pedestrian_light.red_on()
            print u'Uwaga kierowcy'
            # Zółte i czerwone światło dla pojazdów
            traffic_light.yellow_on()
            sleep(0.5)
            # Zielone światło dla pojazdów
            traffic_light.red_off()
            traffic_light.yellow_off()
            traffic_light.green_on()
        else:
            # Ten stan będzie się powtarzał aż do wykrycia kolejnego żądania zmiany świateł przez pieszych
            print u'Można jechać'    
        sleep(1);

except KeyboardInterrupt:
    city.close()
