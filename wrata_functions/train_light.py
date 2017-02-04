# -*- coding: utf-8 -*-

# Moduł obsługujący sygnalizator na przejeździe kolejowym

import city
from time import sleep

def off():
    '''Wyłączenie obu świateł w sygnalizatorze na przejeździe kolejowym'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+2].write(0)
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def on():
    '''Włączenie obu świateł w sygnalizatorze na przejeździe kolejowym'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+2].write(1)
            city.board.digital[p*3+3].write(1)
            return 0            
        p += 1
    return p

def right_on():
    '''Włączenie prawego światła w sygnalizatorze na przejeździe kolejowym'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+2].write(1)
            return 0            
        p += 1
    return p

def right_off():
    '''Wyłączenie prawego światła w sygnalizatorze na przejeździe kolejowym'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+2].write(0)
            return 0            
        p += 1
    return p

def left_on():
    " Włączenie lewego światła w sygnalizatorze na przejeździe kolejowym"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+3].write(1)
            return 0            
        p += 1
    return p

def left_off():
    '''Wyłączenie lewego światła w sygnalizatorze na przejeździe kolejowym'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def blink(count = 5):
    '''Pulsujące naprzemiennie światła w sygnalizatorze na przejeździe kolejowym
         (domyślnie pięć powtórzeń)'''
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 4:
            for i in range(count):
                city.board.digital[p*3+2].write(0)
                city.board.digital[p*3+3].write(1)
                sleep(0.5)
                city.board.digital[p*3+2].write(1)
                city.board.digital[p*3+3].write(0)
                sleep(0.5)
            city.board.digital[p*3+2].write(0)
            return 0            
        p += 1
    return p
