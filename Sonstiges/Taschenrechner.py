#Abfrage
plusminus = raw_input("Moechtest du Addieren?" ' J/N? ')

if plusminus == 'J' or 'j':
    nummer1 = input("Erste Zahl eingeben. ")
    nummer2 = input("Zweite Zahl eingeben. ")
    summe = nummer1 + nummer2

    print "Das Ergebnis ist %d." % (summe)

else:
    nummer1 = input("Erste Zahl eingeben. ")
    nummer2 = input("Zweite Zahl eingeben. ")
    summe = nummer1 - nummer2

    print "Das Ergebnis ist %d." % (summe)