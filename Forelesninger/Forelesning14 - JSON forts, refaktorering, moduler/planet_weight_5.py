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

# Listene med planetnavn og respektive tyngdekrefter
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

#-----------------
# All kode ovenfor er kun definisjoner av funksjoner og variabler og gjør ikke noe 'synlig' i seg selv
# Under kommer koden som kjøres:

# Variabelen run skal styre while-løkka. Så lenge run er True vil løkka gå om igjen og om igjen

run = True
while run == True:
    # Vi kaller funksjonen skriv_header(). Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_header()
    # Vi kaller funksjonen skriv_ut_planetliste(planeter) og sender med lista vår 'planeter' som argument. Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_ut_planetliste(planeter)
    # Vi oppretter en variabel, og denne settes til å inneholde verdien som returneres når vi kaller funksjonen brukerinput_til_index. Stringen vi sender med er argumentet.
    planetnummer = brukerinput_til_index("\nVelg en planet ved å skrive inn et tall: ")

    # Dersom brukeren har valgt 0 for tilfeldig planet vil dette bli lagret som -1 (se definisjonen av funksjonen brukerinput_til_index() ).
    # Vi sjekker derfor om planetnummer er -1, og i så fall velges en tilfeldig planet med funksjonen velg_tilfeldig(), og vi skriver ut hvilken det ble
    if planetnummer == -1:
        valgt_planet = velg_tilfeldig(planeter)
        print(f" Du fikk planeten: {valgt_planet}")
    # Ellers bruker vi planeten brukeren valgte
    else:
        valgt_planet = planeter[planetnummer]
        print(f" Du har valgt: {valgt_planet}")

    # ber om brukerens vekt, gjør den direkte om til float
    brukervekt = float(input("Hva er din vekt på jorden? :"))
    # beregner den nye veklten med funksjonen vi definerte og lagrer det i en variabel. Argumentene vi sender med er vekten som ble skrevet inn og tyngdekraften på den valgte planeten
    vekt_på_annen_planet = beregn_vekt(brukervekt, tyngdekraft[planetnummer])
    print(f"Din vekt på planeten {valgt_planet} vil være {vekt_på_annen_planet} kg")

    # run skal som nevnt styre løkka, her vil verdien til run (True/False) bli bestemt av hva som returneres fra funksjonen vår en_gang_til.
    run = en_gang_til()
