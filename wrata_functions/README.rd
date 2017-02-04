# Program do obsługi zestawu edukacyjnego Inteligentne Miasto (IM)

Sterownik: ArduinoUno z wgranym oprogramowaniem Standard Firmata i nakładką (shieldem) IM.
Do sterownika można maksymalnie podłączyć cztery urządzenia (za pomocą sześciożyłowych przewodów z gniazdami IDC), 
wybrane z siedmiu elementów:
* latarnia uliczna - diody LED (2 x po 3 szt.) i fototranzystor do pomiaru natężenia światła
* czujnik przejazdu - dioda LED IR (emitująca promieniowanie podczerwone) i fototranzystor wykrywający wiązkę promieni IR
* zapora kolejowa - serwo umożliwiające ustawienie zapory pod dowolnym kątem (90 - zapora otwarta, 0 lub 180 - zamknięta)
  i sygnalizacja dźwiękowa (buzzer)
* sygnalizator kolejowy (dla niestrzeżonego przejazdu) - dwie czerwone diody LED
* sygnalizator świetlny dla pieszych - diody czerwona i zielona oraz przycisk żądania zmiany stanu sygnałów
* sygnalizator świetlny dla pojazdów (2 szt.) -  diody czerwona, żółta i zielona

BIBLIOTEKA:

city.py 
Moduł wykorzystywany jest przez pozostałe moduły. łączy program ze sterownikiem Arduino przez port szeregowy,
wykrywa urządzenia podłączone do portów sterownika i wyświetla informacje o tych urządzeniach.
Tworzy zmienną globalną wykorzystywaną w module 'barrier' do pamiętania stanu zapory kolejowej.

barrier.py
Modu� obs�uguje dwa urz�dzenia: zapor� kolejow� i czujnik przejazdu.
Dost�pne w moduje funkcje umo�liwiaj� zamykanie i otwieranie zapory kolejowej, generowanie sygna�u
ostrzegawczego (buzzer w uk�adzie zapory) i wykrywanie przeje�d�aj�cego poci�gu (czujnik przejazdu).

lamp.py
Modu� obs�uguje latarni� uliczn� i jego funkcje umo�liwiaj� w��czanie latarni z pe�n� moc� lub z po�ow� mocy
(tryb ekonomiczny), wy��czanie latarni oraz wykrywanie poziomu nat��enia �wiat�a (ciemno/jasno).

pedestrian_light.py
Modu� obs�uguje sygnalizator �wietlny dla pieszych z przyciskiem ��dania zmiany �wiat�a.

traffic_light.py
Modu� obs�uguje pierwszy (wpi�ty do portu o ni�szym numerze) sygnalizator drogowy
lub pojedynczy sygnalizator (zestaw zawiera dwa sygnalizatory drogowe).

traffic_light2.py
Modu� obs�uguje drugi (wpi�ty do portu o wy�szym numerze) sygnalizator drogowy
lub pojedynczy sygnalizator.

train_light.py
Moduł obsługuje światła na niestrzeżonym przejeździe kolejowym.

PRZYKŁADY STEROWANIA ELEMENTAMI IM:
test_barrier.py
test_lamp.py
test_pedestrian_light.py
test_traffic_light_1.py
test_traffic_light_2.py
test_train_light.py
