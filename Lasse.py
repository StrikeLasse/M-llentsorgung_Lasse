def sensor_pruefen(werte, zeitpunkt, letzte_messung, dauer_einer_woche=7):
    print(f"Zeit: {zeitpunkt} | Werte: {werte}")  
    
    if all(wert == werte[0] for wert in werte):  
        if letzte_messung is None:
            letzte_messung = zeitpunkt  
        elif zeitpunkt - letzte_messung >= dauer_einer_woche:
            return letzte_messung  
    else:
        letzte_messung = None  

    return letzte_messung  

def sensorwerte_eingeben(anzahl_sensoren=7):
    print("Bitte geben Sie die Werte der Sensoren ein:")
    return [int(input(f"Geben Sie den Wert für Sensor {i+1}: ")) for i in range(anzahl_sensoren)]

start_zeit = 0
werte = sensorwerte_eingeben()
start_messung = sensor_pruefen(werte, start_zeit, None)

if all(wert == werte[0] for wert in werte):
    print("WARNUNG! Alle Sensorwerte bleiben seit einer Woche gleich. Nachricht gesendet!")
else:
    print("Alles in Ordnung! Die Sensorenwerte sind nicht identisch über eine Woche hinweg.")