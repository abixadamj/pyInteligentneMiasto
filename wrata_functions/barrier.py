# -*- coding: utf-8 -*-

# Moduł 'barier' do obsługi zestawu Inteligentne Miasto realizuje:
#   - zamykanie i otwieranie zapory kolejowej
#   - generuje sygnał ostrzegawczy (buzzer w układzie zapory)
#   - wykrywa przejeżdżający pociąg (czujnik przejazdu)

import city
from pyfirmata import INPUT, OUTPUT, SERVO
from time import sleep

def open():
    '''Podniesienie (otwarcie) zapory kolejowej'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 3:
            if not(city.isBarrierOpen):
                city.board.digital[p*3+3].mode = SERVO
                city.board.digital[p*3+3].write(90)
                city.isBarrierOpen = True
            return 0            
        p += 1
    return p

def close_left():
    '''Zamknięcie zapory w lewo'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 3:      
            city.board.digital[p*3+3].mode = SERVO
            city.board.digital[p*3+3].write(180)
            city.isBarrierOpen = False
            return 0            
        p += 1
    return p

def close_right():
    '''Zamknięcie zapory w prawo'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 3:
            city.board.digital[p*3+3].mode = SERVO
            city.board.digital[p*3+3].write(0)
            city.isBarrierOpen = False
            return 0            
        p += 1
    return p

def beacon():
    '''Sygnał ostrzegawczy'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        sleep(0.2)
        if  x == 3:
            city.board.digital[p*3+2].mode = OUTPUT
            for i in range(4):
                city.board.digital[p*3+2].write(1)
                sleep(0.3)
                city.board.digital[p*3+2].write(0)
                sleep(0.1)
            return 0            
        p += 1
    return p

def is_train():
    '''Detekcja przejeżdząjącego pociągu - czujnik przejazdu'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 2:
            city.board.digital[p*3+2].mode = INPUT
            city.board.digital[p*3+2].enable_reporting()
            if  city.board.digital[p*3+2].read() == 1:
                return True
            else:                
                return False
        p += 1
    return False


