# -*- coding: utf-8 -*-

# Przykład z sygnalizatorem kolejowym i czujnikiem przejazdu

# Import modułów programu
import city
import train_light
import barrier

from time import sleep

# Lista dostępnych urządzeń
city.info()

print(u'Testowanie sygnalizatora - 1')
# Naprzemienne pulsowanie świateł - 5 s (5 zmian)
for i in range(5):
    train_light.left_on()
    train_light.right_off()
    sleep(0.5)
    train_light.left_off()
    train_light.right_on()
    sleep(0.5)
# Wyłączenie sygnalizatora    
train_light.off()   

print(u'Testowanie sygnalizatora - 2')
# Naprzemienne pulsowanie świateł - 3 s (funkcja blink())
train_light.blink(3)

print(u'Testowanie sygnalizatora - 3')
# Włączenie obu świateł - 2 s 
train_light.on()
sleep(2)
train_light.off()

try:
    # Włączanie sygnalizatora, gdy zbliża się pociąg
    print(u'Detektor pociągu włączony:')
    while True:
        if barrier.is_train():
            print(u'zbliża się pociąg')
            train_light.blink() # domyślnie 5 s
        else:
            print(u'przejazd wolny')
            train_light.off() # można pominąć, blink() wyłączy światła
        
except KeyboardInterrupt:
    city.close()
