# -*- coding: utf-8 -*-

# Przykład sterowania latarnią uliczną

# Import modułów programu
import city
import lamp
from time import sleep

# Lista dostępnych urządzeń
city.info()

print(u'Włączenie latarni ulicznej z pełną mocą')
# Włączenie latarni ulicznej - pełna moc świecenia
lamp.on()
sleep(3)

print(u'Włączenie latarni ulicznej z połową mocy')
# Włączenie latarni ulicznej - tryb ekonomiczny
lamp.on_eco()
sleep(3)

print(u'Wyłączenie latarni ulicznej')
# Wyłączenie latarni ulicznej
lamp.off()
sleep(3)

try:
    # Włączanie/wyłączenie latarni ulicznej w zależności od natężenia światła w otoczeniu
    print(u'Automatyczne sterowanie latarnią uliczną - pomiar natężenia światła')
    while True:
        if lamp.is_dark():
            print(u'jest ciemno')
            lamp.on()
        else:
            print(u'jest jasno')
            lamp.off()
        sleep(0.5) # pomiar natężenia co pół sekundy
        
except KeyboardInterrupt:
    city.close()
