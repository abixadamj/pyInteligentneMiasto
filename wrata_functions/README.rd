#Program do obsługi zestawu edukacyjnego Inteligentne Miasto (IM)

Sterownik: ArduinoUno z wgranym oprogramowaniem Standard Firmata i nak�adk� (shieldem) IM.
Do sterownika mo�na maksymalnie pod��czy� cztery urz�dzenia (za pomoc� sze�cio�y�owych przewod�w z gniazdami IDC), 
wybrane z siedmiu element�w:
* latarnia uliczna - diody LED (2 x po 3 szt.) i fototranzystor do pomiaru nat��enia �wiat�a
* czujnik przejazdu - dioda LED IR (emituj�ca promieniowanie podczerwone) i fototranzystor wykrywaj�cy wi�zk� promieni IR
* zapora kolejowa - serwo umo�liwiaj�ce ustawienie zapory pod dowolnym k�tem (90 - zapora otwarta, 0 lub 180 - zamkni�ta)
  i sygnalizacja d�wi�kowa (buzzer)
* sygnalizator kolejowy (dla niestrze�onego przejazdu) - dwie czerwone diody LED
* sygnalizator �wietlny dla pieszych - diody czerwona i zielona oraz przycisk ��dania zmiany stanu sygna��w
* sygnalizator �wietlny dla pojazd�w (2 szt.) -  diody czerwona, ���ta i zielona

BIBLIOTEKA:

city.py 
Modu� wykorzystywany jest przez pozosta�e modu�y. ��czy program ze sterownikiem Arduino przez port szeregowy,
wykrywa urz�dzenia pod��czone do port�w sterownika i wy�wietla informacje o tych urz�dzeniach.
Tworzy zmienn� globaln� wykorzystywan� w module 'barrier' do pami�tania stanu zapory kolejowej.

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
Modu� obs�uguje �wiat�a na niestrze�onym przeje�dzie kolejowym.

PRZYK�ADY STEROWANIA ELEMENTAMI IM:
test_barrier.py
test_lamp.py
test_pedestrian_light.py
test_traffic_light_1.py
test_traffic_light_2.py
test_train_light.py
