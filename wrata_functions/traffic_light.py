# -*- coding: utf-8 -*-

# Moduł obsługujący pierwszy (wpięty do portu o niższym numerze)
# lub pojedynczy sygnalizator drogowy w zestawie Inteligentne Miasto

from time import sleep
import city

def off():
    "Wyłączenie wszystkich świateł"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+2].write(0)
            city.board.digital[p*3+3].write(0)
            city.board.digital[p*3+4].write(0)
            return 0            
        p += 1
    return p

def red_on():
    "Włączenie czerwonego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+2].write(1)
            return 0            
        p += 1
    return p

def red_off():
    "Wyłączenie czerwonego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+2].write(0)
            return 0            
        p += 1
    return p

def yellow_on():
    "Włączenie żółtego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+3].write(1)
            return 0            
        p += 1
    return p

def yellow_off():
    "Wyłączenie żółtego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def yellow_blink(count = 3):
    "Włączenie żółtego pulsującego światła - domyślnie 3 błyski"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            for i in range(count):
                city.board.digital[p*3+3].write(1)
                sleep(0.5)
                city.board.digital[p*3+3].write(0)
                sleep(0.5)
            return 0            
        p += 1
    return p

def green_on():
    "Włączenie zielonego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 6:
            city.board.digital[p*3+4].write(1)
            return 0            
        p += 1
    return p

def green_off():
    "Wyłączenie zielonego światła"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        sleep(0.2)
        if  x == 6:
            city.board.digital[p*3+4].write(0)
            return 0            
        p += 1
    return p

