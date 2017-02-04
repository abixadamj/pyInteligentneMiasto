#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyIntelligentCity.py
#  
#  Copyright 2017 ABIX Adam Jurkiewicz <python@cyfrowaszkola.waw.pl>
#  Portions code (functions) Copyright 2017 Wiesław Rychlicki <wrata@poczta.onet.pl>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# 
#

from pyfirmata import Arduino, util, OUTPUT
from time import sleep
import sys


class pyIntelligentCity(object):
    '''
    Klasa pyIntelligentCity - obsługa zestawu edukacyjnego Inteligentne Miasto
    '''
      
    def __init__(self,ComPort):
        '''
        comPort: '/dev/ttyUSB0' for Linux, 'COM1' for Windows
        sys.platform - oddaje system
        Weryfikujemy, co jest podłączone i budujemy słownik Devices
        '''
        self.ComPort = ComPort
        self.IsCity = False
        
        # jakie urządzenia są aktualnie podłączone 
        self.Devices = None
        self.DevicesNames = None
        self.DefDevicesNames = [     
            'Nieznany element albo pusty port',
            'Lampa uliczna',
            'Czujnik przejazdu',
            'Zapora kolejowa',
            'Sygnalizator kolejowy',
            'Sygnalizator dla pieszych',
            'Sygnalizator drogowy'
        ]
                
        # test
        self.IsCity = self.arduino_detect()
        self.device_detect()
        
       
    ###################################################################

    def close(self):
        self.board.exit()
        
    def arduino_detect(self):
        try:
            self.board = Arduino(self.ComPort)
            self.iterator = util.Iterator(self.board)
            self.iterator.start()
            # Otwiera piny analogowe A0, A1, A2 i A3 do odczytu danych w celu dekodowania urządzeń
            for x in [0, 1, 2, 3]:
                self.board.analog[x].enable_reporting()
            # ustawiamy wszystkie podłączone urządzenia 
            print('Done OK - connecting Arduino with IntelligentCity at COM Port: ' + self.ComPort) 
            return True
        except:
            print('City not found')
            return False
                    
    def device_detect(self):
        '''
        Sprawdzamy co jest podłączone. Parametr a = 0..1023 - odczytany z pinów analogowego (A0..A3) w porcie urządzenia
        '''
        if not self.IsCity:
            print('Cannot detect - there is no Arduino connected at: '+ self.ComPort)
            return None
        ret_val = None
        device_type = []
        for port in range(4):
            ret_val = None
            while type(ret_val) != float:
                ret_val = self.board.analog[port].read()
            a = int(ret_val * 1023)
            #print(port, a)
            if a <=1010 and a >=990: # sygnalizator drogowy
                device_type.append(6)
            elif a <=985 and a >=965: # sygnalizator dla pieszych
                device_type.append(5)
            elif a <=960 and a >=940: # sygnalizator kolejowy
                device_type.append(4)
            elif a <=931 and a >=911: # zapora kolejowa
                device_type.append(3)
            elif a <=890 and a >=860: # czujnik przejazdu
                device_type.append(2)
            elif a <=600:   # lampa uliczna (może być też pusty port!)
                device_type.append(1)
            else: # nieznane urządzenie lub pusty port
                device_type.append(0)
        # po przejściu wszystkich 4 portów zapisujemy słownik definiujący typy oraz opisy urządzeń
        self.Devices = {
                        0 : device_type[0],
                        1 : device_type[1],
                        2 : device_type[2],
                        3 : device_type[3]
                       }
        self.DevicesNames = {
                             0: self.DefDevicesNames[device_type[0]],
                             1: self.DefDevicesNames[device_type[1]],
                             2: self.DefDevicesNames[device_type[2]],
                             3: self.DefDevicesNames[device_type[3]]
                            }   
           
    def info(self):
        '''
        Wypisujemy wszystkie informacje o podłączonym mieście
        '''
        if not self.IsCity:
            print('There is NO City connected. Bye bye ...')
            return False
        else:
            print('There is city connected at port: '+ self.ComPort)
            print u'Wykryte elementy Inteligentnego Miasta:'
            for port in [0, 1, 2, 3]:
                print (port, self.Devices[port], self.DevicesNames[port])
            return True

    ################################
    # Sterowanie latarnią uliczną  #
    
    def lamp_off(self):
        ''' Latarnia uliczna - wyłączenie latarni '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 1: # latarnia uliczna
                self.board.digital[p*3+2].write(0)
                self.board.digital[p*3+3].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono
    
    def lamp_on(self):
        ''' Latarnia uliczna - włączenie latarni z pełną mocą '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 1: # latarnia uliczna
                self.board.digital[p*3+2].write(1)
                self.board.digital[p*3+3].write(1)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

    def lamp_eco_on(self):
        ''' Latarnia uliczna - włączenie latarni w trybie ekonomicznym '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 1: # latarnia uliczna
                self.board.digital[p*3+2].write(1)
                self.board.digital[p*3+3].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

    def isDark(self):
        ''' Latarnia uliczna - pomiar natężenia światła w otoczeniu '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 1:
                a = int(self.board.analog[p].read() * 1023)
                if a < 105: # można ustalić inny poziom
                    return True   # ciemno
                else:
                    return False # jasno
            p += 1
        return False # lampa nie jest podłączona do sterownika
            
    
    #########################################    
    # Sterowanie sygnalizatorem drogowym SD #

    def SD_all_off(self):
        ''' Sygnalizator drogowy - wyłączenie wszystkich świateł '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+2].write(0)
                self.board.digital[p*3+3].write(0)
                self.board.digital[p*3+4].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono    

    def SD_red_on(self):
        ''' Sygnalizator drogowy - włączenie czerwonego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+2].write(1)
                return p   # zwraca numer portu 0, 1, 2 lub 3         
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

    def SD_red_off(self):
        ''' Sygnalizator drogowy - wyłączenie czerwonego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+2].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono    

    def SD_yellow_on(self):
        ''' Sygnalizator drogowy - włączenie żółtego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+3].write(1)
                return p   # zwraca numer portu 0, 1, 2 lub 3         
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

    def SD_yellow_off(self):
        ''' Sygnalizator drogowy - wyłączenie żółtego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+3].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono    

    def SD_yellow_blink(self,time=5):
        ''' Sygnalizator drogowy - włączenie pulsującego żółtego światła - 5 s '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                for n in range(time):
                    self.board.digital[p*3+3].write(1)
                    sleep(0.5)
                    self.board.digital[p*3+3].write(0)
                    sleep(0.5)
                return p   # zwraca numer portu 0, 1, 2 lub 3         
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono
    
    def SD_green_on(self):
        ''' Sygnalizator drogowy - włączenie zielonego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+4].write(1)
                return p   # zwraca numer portu 0, 1, 2 lub 3         
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

    def SD_green_off(self):
        ''' Sygnalizator drogowy - wyłączenie zielonego światła '''
        p = 0    
        while p < 4:
            if  self.Devices[p] == 6: # sygnalizator drogowy
                self.board.digital[p*3+4].write(0)
                return p   # zwraca numer portu 0, 1, 2 lub 3          
            p += 1
        return p  # zwraca 4 - urządzenia nie podłączono

def main(args):
    city = pyIntelligentCity('COM5')
    print('\n')
    city.info()
    city.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
