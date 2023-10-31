# Dette er den nye modulen. Hører sammen med planet_weight_6.py.
# Her finner vi igjen alle funksjonsdefinisjonene vi tidligere hadde i hovedfilen.

import random

# definerer en funksjon som skal skrive ut en "fin" overskrift til brukeren
# Funksjonen trenger ikke returnere noen verdi
def skriv_header():
    print("\n ========================================")
    print(" == Hva er din vekt på en annen planet? ==")
    print("===========================================")

# definerer en funksjon som skal skrive ut planetene fra en liste
# Funksjonen har 1 parameter, og denne er tenkt å være en liste
# Funksjonen trenger ikke returnere noen verdi
def skriv_ut_planetliste(planeter_som_skal_printes):
    print("0 - Tilfeldig planet")
    for planetnummer, planet in enumerate(planeter_som_skal_printes):
        print(f"{planetnummer + 1} - {planet}")

# definerer en funksjon som skal be brukeren om å skrive inn et tall.
# Tallet skal vi så bruke som indexnummer for å finne rett planet fra lista (vi må derfor trekke fra 1).
# Funksjonen skal returnere det beregnede indexnummeret som heltall (int)
# Funksjonen har 1 parameter, og denne er tenkt å være en string, som vi sender med når vi kaller funksjonen
def brukerinput_til_index(beskjed):
    planetnummer = input(beskjed)
    index = int(planetnummer) -1
    return index

# definerer en funksjon som skal velge en tilfeldig planet fra lista.
# funksjonen har 1 parameter, og denne er tenkt å være en liste (listen med planeter)
# Bruker randrange() for å velge et tilfeldig tall mellom 0 og antall elementer i lista
# Funksjonen skal returnere navnet på den tilfeldig valgte planeten (string)
def velg_tilfeldig(valgt_liste):
    index = random.randrange(0, len(valgt_liste))
    valgt_element = valgt_liste[index]
    return valgt_element

# definerer en funksjon som skal beregne brukerens vekt på den valgte planeten
# funksjonen har 3 parametere: brukerens vekt, tyngdekraften på valgt planet og jordens tyngdekraft
# Den tredje parameteren, jordens tyngdekraft, setter vi en standardverdi for (=9,807). Det innebærer at dersom vi kun sender med 2 argumenter når vi kaller funksjonen, så vil den bruke standardvedien vi satt for jordens tyngdekraft som den tredje parameteren)
# Legg merke til at vi bruker de interne variabelnavnene våre (fra parameterne) når vi gjør beregningen
# Funksjonen skal returnere den beregnede vekten, avrundet til 2 desimaler (float)
def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    beregnet_vekt = din_vekt / jordtyngdekraft * planettyngdekraft
    return round(beregnet_vekt, 2)

# definerer en funksjon for å styre hvorvidt løkka (og dermed programmet vårt) skal kjøre en gang til
# Vi ber brukeren om å skrive inn Y eller N.
# Ved å omgjøre brukerens input til store bokstaver med upper() vil både stor og liten y godkjennes for å kjøre en gang til
# Funksjonen skal returnere enten True eller False (bool) basert om om brukerens input var Y eller ikke.
def en_gang_til():
    svar = input("Vil du prøve igjen? (Y/N ")
    return svar.upper() == 'Y'
