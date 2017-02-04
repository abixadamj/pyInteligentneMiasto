#Program do obsługi zestawu edukacyjnego<br />Inteligentne Miasto (IM)
<hr />
###Sterownik

*ArduinoUno* z wgranym oprogramowaniem *Standard Firmata* i nakładką (shieldem) *Inteligentne Miasto*.
Do sterownika można maksymalnie podłączyć cztery urządzenia (za pomocą sześciożyłowych przewodów z gniazdami IDC), 
wybrane z siedmiu elementów:
* *latarnia uliczna* - diody LED (2 x po 3 szt.) i fototranzystor do pomiaru natężenia światła
* *czujnik przejazdu* - dioda LED IR (emitująca promieniowanie podczerwone) i fototranzystor wykrywający wiązkę promieni IR
* *zapora kolejowa* - serwo umożliwiające ustawienie zapory pod dowolnym kątem (90 - zapora otwarta, 0 lub 180 - zamknięta)
  i sygnalizacja dźwiękowa (buzzer)
* *sygnalizator kolejowy* (dla niestrzeżonego przejazdu) - dwie czerwone diody LED
* *sygnalizator świetlny dla pieszych* - diody czerwona i zielona oraz przycisk żądania zmiany stanu sygnałów
* *sygnalizator świetlny dla pojazdów* (2 szt.) -  diody czerwona, żółta i zielona
![rys](www.biblioteka.lesko.pl/gopro/f02_17/001.jpg)
<hr />
###Biblioteka

*city.py* - główny moduł wykorzystywany przez pozostałe moduły. Łączy program ze sterownikiem Arduino przez port szeregowy,
wykrywa urządzenia podłączone do portów sterownika i wyświetla informacje o tych urządzeniach.
Tworzy zmienną globalną wykorzystywaną w module *barrier* do pamiętania stanu zapory kolejowej.

*barrier.py* - moduł obsługuje dwa urządzenia: zaporę kolejową i czujnik przejazdu.
Dostępne w moduje funkcje umożliwiają zamykanie i otwieranie zapory kolejowej, generowanie sygnału
ostrzegawczego (buzzer w układzie zapory) i wykrywanie przejeżdżajżcego pociągu (czujnik przejazdu).

*lamp.py* - moduł obsługuje latarnię uliczną i jego funkcje umożliwiają włączanie latarni z pełną mocą lub z połową mocy
(tryb ekonomiczny), wylączanie latarni oraz wykrywanie poziomu natężenia światła (ciemno/jasno).

*pedestrian_light.py* - moduł obsługuje sygnalizator świetlny dla pieszych z przyciskiem żądania zmiany światła.

*traffic_light.py*
Moduł obsługuje pierwszy (wpięty do portu o niższym numerze) sygnalizator drogowy
lub pojedynczy sygnalizator (zestaw zawiera dwa sygnalizatory drogowe).

*traffic_light2.py* - moduł obsługuje drugi (wpięty do portu o wyższym numerze) sygnalizator drogowy
lub pojedynczy sygnalizator.

*train_light.py* - moduł obsługuje światła na niestrzeżonym przejeździe kolejowym.

<hr />
###Przykłady sterowania elementami zestawu IM

*test_barrier.py* - przykład sterowania *zaporą kolejową* i *czujnikiem przejazdu*.

*test_lamp.py* - przykład sterowania *latarnią uliczną* z czujnikiem natężenia światła w otoczeniu.

*test_pedestrian_light.py* - przykład wykorzystania *sygnalizatora na przejściu dla pieszych* współpracującego z *sygnalizatorem drogowym* dla samochodów. Zielone światło dla pieszych włączane jest na żądanie, po maciśnięciu przycisku w sygnalizatorze. Światła *sygnalizatora drogowego* są zsynchronizowane z światłem *sygnalizatora dla pieszych*.

*test_traffic_light_1.py* - przykład sterowania *sygnalizatorem drogowym* - cykliczna zmiana świateł.

*test_traffic_light_2.py* - przykład sterowania dwoma *sygnalizatorami drogowymi* z cykliczną zmianą świateł na skrzyżowaniu.

*test_train_light.py* - przykład sterowania *sygnalizatorem kolejowym* ustawionym przed niestrzeżonym przejazdem kolejowym i współpracującym  z *czujnikiem przejazdu*, który wykrywa nadjeżdżający pociąg.
