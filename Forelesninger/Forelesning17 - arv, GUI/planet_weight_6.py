# Dette er hovedfilen vår. Funksjonsdefinisjonene har vi flyttet over i en ny fil/modul, 'planetfunksjoner'.

# Importerer alt innhold fra 'planetfunksjoner. * er et wildcard og brukes der vi ikke ønsker/kan spesifisere.
from planetfunksjoner import *

# Listene med planetnavn og respektive tyngdekrefter
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

#-----------------
# All kode ovenfor er kun definisjoner av funksjoner og variabler og gjør ikke noe 'synlig' i seg selv
# Under kommer koden som kjøres, og som er selve programmet

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
