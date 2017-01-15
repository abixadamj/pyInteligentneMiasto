# -*- coding: utf-8 -*-

# Moduł 'pedestrian_light' obsługuje sygnalizator świetlny dla pieszych
# z przyciskiem żądania zmiany światła

# Import modułów i stałych z modułu pyfirmata
import city
from pyfirmata import INPUT, OUTPUT
from time import sleep

def red_on():
    "Włączenie światła czerwonego"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        sleep(0.2)
        if  x == 5:
            city.board.digital[p*3+2].write(1)
            return 0            
        p += 1
    return p

def red_off():
    "Wyłączenie światła czerwonego"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 5:
            city.board.digital[p*3+2].write(0)
            return 0            
        p += 1
    return p

def green_on():
    "Włączenie światła zielonego"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 5:
            city.board.digital[p*3+3].write(1)
            return 0            
        p += 1
    return p

def green_off():
    "Wyłączenie światła zielonego"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 5:
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def green_blink(count = 2):
    "Włączenie pulsującego światła zielonego - domyślnie 2 s"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 5:
            for i in range(count*2):
                sleep(0.25)
                city.board.digital[p*3+3].write(0)
                sleep(0.25)
                city.board.digital[p*3+3].write(1)
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def is_pressed():
    "Odczytywanie stanu przycisku w sygnalizatorze"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 5:
            # ustawienie pinu cyfrowego w trybie wejścia - przycisk
            city.board.digital[p*3+4].mode = INPUT
            city.board.digital[p*3+4].enable_reporting()
            # odczyt stanu pinu cyfrowego - stan przycisku
            button = city.board.digital[p*3+4].read()
            if  button == 1:
                return True  # przycisk naciśnięty
            else:                
                return False # przycisk zwolniony
        p += 1
    return False # urządzenie nie jest podłączone do sterownika


