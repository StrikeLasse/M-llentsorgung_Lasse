werte = []  
dauer_einer_woche = 7  

# Benutzer gibt die Werte für die 7 Sensoren ein
for i in range(7):
    wert = int(input(f"Gib den Wert für Sensor {i+1} ein: "))
    werte.append(wert)

start_messung = None  

def sensor_pruefen(neue_werte, zeitpunkt, letzte_messung):
    print(f"Zeit: {zeitpunkt} | Werte: {neue_werte}")  
    
    if all(wert == neue_werte[0] for wert in neue_werte):  
        if letzte_messung is None:
            letzte_messung = zeitpunkt  
        elif zeitpunkt - letzte_messung >= dauer_einer_woche:
            return letzte_messung  
    else:
        letzte_messung = None  

    return letzte_messung  

start_zeit = 0

start_messung = sensor_pruefen(werte, start_zeit, start_messung)

if all(wert == werte[0] for wert in werte):
    print("WARNUNG! Alle Sensorwerte bleiben seit einer Woche gleich. Nachricht gesendet!")
else:
    print("Alles in Ordnung! Sensorwerte sind nicht identisch.")
    
print("Ich werde Sie nun nach sieben Sensorwerten fragen. Normalerweise würden diese Werte automatisch ausgelesen werden, aber da wir hier eine Demonstration machen und die Sensoren nicht programmieren, sondern Beispielwerte verwenden, geben Sie diese bitte manuell ein.")

werte = []  
dauer_einer_woche = 7  

# Benutzer gibt die Werte für die 7 Sensoren ein
for i in range(7):
    wert = int(input(f"Geben Sie den Wert für Sensor {i+1} ein: "))
    werte.append(wert)

start_messung = None  

def sensor_pruefen(neue_werte, zeitpunkt, letzte_messung):
    print(f"Zeit: {zeitpunkt} | Werte: {neue_werte}")  
    
    if all(wert == neue_werte[0] for wert in neue_werte):  
        if letzte_messung is None:
            letzte_messung = zeitpunkt  
        elif zeitpunkt - letzte_messung >= dauer_einer_woche:
            return letzte_messung  
    else:
        letzte_messung = None  

    return letzte_messung  

start_zeit = 0

start_messung = sensor_pruefen(werte, start_zeit, start_messung)

if all(wert == werte[0] for wert in werte):
    print("WARNUNG! Alle Sensorwerte bleiben seit einer Woche gleich. Nachricht gesendet!")
else:
    print("Alles in Ordnung! Sensorwerte sind nicht identisch.")