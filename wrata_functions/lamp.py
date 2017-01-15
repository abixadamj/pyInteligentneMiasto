# -*- coding: utf-8 -*-

# Moduł 'lamp' do obsługi zestawu Inteligentne Miasto realizuje:
#   - włączanie latarni ulicznej z pełną mocą
#   - włączanie latarni ulicznej z połową mocy (tryb ekonomiczny)
#   - wyłączanie latarni ulicznej
#   - wykrywanie poziomu natężenia światła (ciemno/jasno)

from time import sleep
import city

def on():
    "Włączenie lampy"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 1:
            city.board.digital[p*3+2].write(1)
            city.board.digital[p*3+3].write(1)
            return 0            
        p += 1
    return p      

def off():
    "Wyłączenie lampy"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 1:
            city.board.digital[p*3+2].write(0)
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def on_eco():
    "Włączenie lampy w trybie oszczędnościowym (połowa diod)"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 1:
            city.board.digital[p*3+2].write(1)
            city.board.digital[p*3+3].write(0)
            return 0            
        p += 1
    return p

def is_dark():
    "Wykrywanie poziomu natężenia światła w otoczeniu lampy"
    p = 0    
    while p < 4:
        a = city.read_port(p)
        x = city.device_detect(a)
        if  x == 1:
            if a < 105: # można ustalić inny poziom
                return True   # ciemno
            else:
                return False # jasno
        p += 1
    return False # lampa nie jest podłączona do sterownika
