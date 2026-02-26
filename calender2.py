from datetime import datetime
abschluss_text = input("Wann ist Dein Abschluss? ")
abschluss_datum = datetime.strptime(abschluss_text,"%d,%m,%Y")
heute = datetime.now()
zeitspanne =  abschluss_datum - heute
print(f"Bis Dein Abschluss sind {zeitspanne.days} geblieben")

#Benutzer hat Flug am 28.02.2026 um 12.18, gebe aus, wie viel Zeit ist ihm geblieben

Du hast Dein Flug in: xxxx

login = {"steffan":"steffan1986",
         "feltMirNicht1":"feltMir1",
         "lenny":"maedchen"}

