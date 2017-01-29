"""
Copyright 2017 ABIX Adam Jurkiewicz <python@cyfrowaszkola.waw.pl>
Portions code (functions):
Copyright 2017 Wiesław Rychlicki <wrata@poczta.onet.pl>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

from pyfirmata import Arduino, util
import sys


class pyIntelligentCity(object):
    '''
    Klasa pyIntelligentCity - obsługa Inteligentnego Miasta
    '''
    # ważne definicje:
    NIC = 0
    LAMPA = 1
    CZUJNIK = 2
    ZAPORA = 3
    SYGN_KOLEJOWY = 4
    SYGN_PIESZYCH = 5
    SYGN_DROGOWY = 6

    def __init__(self, ComPort):
        '''
        comPort: '/dev/ttyUSB0' for Linux, 'COM1' for Windows
        sys.platform - oddaje system
        Weryfikujemy, co jest podłączone, ustawiamy słownik Devices
        '''
        self.ComPort = ComPort
        self.IsCity = False
        self.IsBarrier = False
        self.IsNight = False
        self.IsLampConnected = False
        # jakie urządzenia są aktualnie podłączone
        self.Devices = None
        self.DevicesNames = None
        self.DefDevicesNames = [
            'Not implemented ;-) Yet.... ',
            'Lampa uliczna',
            'Czujnik przejazdu',
            'Zapora kolejowa',
            'Sygnalizator kolejowy',
            'Sygnalizator dla pieszych',
            'Sygnalizator drogowy',
        ]

        # test
        self.arduino_detect()
        self.device_detect()

        # jesli jest miasto
        if self.IsCity:
            self.iterator = util.Iterator(self.board)
            self.iterator.start()
            # Otwiera pinów analogowe A0, A1, A2 i A3 do odczytu danych \
            # w celu dekodowania urządzeń
            for x in [0, 1, 2, 3]:
                self.board.analog[x].enable_reporting()
            # ustawiamy wszystkie podłączone urządzenia
            self.device_detect()

    ###################################################################
    def close(self):
        self.board.exit()

    def arduino_detect(self):
        try:
            self.board = Arduino(self.ComPort)
            self.IsCity = True
            print('Done OK - connecting \
            Arduino with IntelligentCity at COM Port: ' + self.ComPort)
            return True
        except:
            self.IsCity = False
            print('City not found')
            return False

    def device_detect(self):
        '''
        Sprawdzamy co jest podłączone. Parametr a = 0..1023 -
        odczytany z pinów analogowego (A0..A3) w porcie urządzenia
        '''
        if not self.IsCity:
            print('Cannot detect - there is no Arduino \
            connected at: ' + self.ComPort)
            return None
        ret_val = None
        device_type = []
        for port in range(4):
            ret_val = None
            while type(ret_val) != float:
                ret_val = self.board.analog[port].read()
            a = int(ret_val * 1023)
            if a <= 1010 and a >= 990:  # sygnalizator drogowy
                device_type.add(6)
            elif a <= 985 and a >= 965:  # sygnalizator dla pieszych
                device_type.add(5)
            elif a <= 960 and a >= 940:  # sygnalizator kolejowy
                device_type.add(4)
            elif a <= 931 and a >= 911:  # zapora kolejowa
                device_type.add(3)
            elif a <= 890 and a >= 860:  # czujnik przejazdu
                device_type.add(2)
            elif a <= 600 and a >= 100:  # lampa uliczna (lub pusty port!)
                device_type.add(1)
            else:  # nieznane urządzenie lub pusty port
                return 0
        # po przejściu wszystkich 4 portów zapisujemy słownik definiujący
        # typy oraz opisy urządzeń
        self.Devices = {
                        0: device_type[0],
                        1: device_type[1],
                        2: device_type[2],
                        3: device_type[3]
                        }
        self.DevicesNames = {
                            0: self.DefDevicesNames[device_type[0]],
                            1: self.DefDevicesNames[device_type[1]],
                            2: self.DefDevicesNames[device_type[2]],
                            3: self.DefDevicesNames[device_type[3]],
                            }
        # over

    def IsCityConnected(self):
        if self.arduino_detect():
            return True
        else:
            return False

    def IsLampConnected(self):
        return self.IsLampConnected

    def info(self):
        '''
        Wypisujemy wszystkie informacje o podłączonym mieście,
        o ile w ogóle jest
        '''
        if not self.IsCity:
            print('There is NO City connected. Bye bye ...')
            return False
        else:
            print('There is city connected at port: ' + self.ComPort)
            return True

    ############################
    # Sterowanie ...
    def LampaUliczna_Red(self, state):
        for pos in self.Devices.listitems():
            x, y = pos
            # tu dokończyć.......


def main(args):

    city = pyIntelligentCity('/dev/ttyUSB3')
    print('-----')
    city.info()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
