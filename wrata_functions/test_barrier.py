# -*- coding: utf-8 -*-

# Przykład z zaporą i czujnikiem przejazdu

# Import modułów programu
import city
import barrier

from time import sleep

# Lista dostępnych urządzeń
city.info()

print(u'Testowanie zapory:')

try:
    barrier.open()
    print u'zapora otwarta'
    sleep(2)
    
    barrier.close_left()
    print u'zapora zamknięta w lewo'
    sleep(2)

    barrier.open()
    print u'zapora otwarta'
    sleep(2)

    barrier.close_right()
    print u'zamknięta w prawo'
    sleep(2)

    barrier.open()
    print u'zapora otwarta'
    sleep(2)
    
    print(u'Detektor pociągu włączony:')
    while True:
        if barrier.is_train():
            print(u'zbliża się pociąg')
            barrier.beacon()
            barrier.close_left()
            sleep(2)
        else:
            print(u'przejazd wolny')
            barrier.open()
        
except KeyboardInterrupt:
    city.close()
