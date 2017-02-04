# -*- coding: utf-8 -*-

# Moduł 'city' do obsługi zestawu Inteligentne Miasto realizuje:
#   - połączenie programu ze sterownikiem Arduino przez port szeregowy
#   - wykrywanie urządzeń podłączonych do portów sterownika
#   - wyświetlanie informacji o urządzeniach
#   - tworzenie zmiennej wykorzystywanej w module 'barrier' do pamiętania stanu zapory

from pyfirmata import Arduino, util, OUTPUT
from time import sleep

# Otwiera połączenie z Arduino
board = Arduino('COM22') # Wpisz odpowiednią nazwę portu szeregowego
iterator = util.Iterator(board)
iterator.start()

# Globalna zmienna do zapamiętania stanu zapory kolejowej
global isBarrierOpen
isBarrierOpen = False

# Otwiera piny analogowe A0, A1, A2 i A3 do odczytu danych w celu dekodowania urządzeń
for x in [0, 1, 2, 3]:
    board.analog[x].enable_reporting()

def device_detect (a): 
    '''Zwraca kod urządzenia. Parametr a = 0..1023 - odczytany z pinu analogowego w porcie urządzenia'''
    if a <=1010 and a >=990: # sygnalizator drogowy
        return 6
    elif a <=985 and a >=965: # sygnalizator dla pieszych
        return 5
    elif a <=960 and a >=940: # sygnalizator kolejowy
        return 4
    elif a <=931 and a >=911: # zapora kolejowa
        return 3
    elif a <=890 and a >=860: # czujnik przejazdu
        return 2
    elif a <=600:   # lampa uliczna (może być też pusty port!)
        return 1
    else: # nieznane urządzenie lub pusty port
        return 0 

def device_name (kod):
    '''Zwraca nazwę urządzenia o podanym kodzie - parametr kod'''
    if kod == 6:
        return 'sygnalizator drogowy'
    elif kod == 5:
        return 'sygnalizator dla pieszych'
    elif kod == 4:
        return 'sygnalizator kolejowy'
    elif kod == 3:
        return 'zapora kolejowa'
    elif kod == 2:
        return 'czujnik przejazdu'
    elif kod == 1:
        return 'lampa uliczna'
    else:
        return 'Hmm, tego ustrojstwa nie znam :('

def read_port(p):
    '''Zwraca wartość odczytaną z pinu analogowego w porcie p, (p = 0, 1, 2 i 3)'''
    odp = board.analog[p].read()
    while type(odp) != float:
        odp = board.analog[p].read()
    return int(odp * 1023)

def info():
    '''Wyświetla listę urządzeń podłączonych do Arduino'''
    print u'Inteligentne Miasto - urządzenia gotowe do pracy:'
    for p in [0, 1, 2, 3]:
        print 'Port', p, ': ', device_name(device_detect(read_port(p)))

def close():
    '''Wyłącza wszystkie urządzenia i zamyka połączenie z Arduino'''
    for p in range(2, 14):
        board.digital[p].mode = OUTPUT
        board.digital[p].write(0)
    print u'Inteligentne Miasto odłączone!'
    board.exit()   

if __name__ == "__main__":
    info()
