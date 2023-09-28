
# Lister med planetnavn og deres tyngdekraft
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

# Programmet skal gå helt til brukeren ønsker å avslutte det.
# Vi løser dette ved å legge all koden for programmet i en while-løkke (legg merke til indenteringen!).
# Variabelen 'kjør' skal vi bruke til å styre hvorvidt løkka (og dermed programmet) skal avsluttes, basert på input fra bruker


kjør = True
while kjør:  # Dette er det samme som while kjør == True:
    print("\n ========================================")
    print(" == Hva er din vekt på en annen planet? ==")
    print("===========================================")

    # Vi skriver ut nummer og hvilke planeter brukeren kan velge
    for planetnummer in range(len(planeter)):
        print(f"{planetnummer + 1} - {planeter[planetnummer]}")

    # Ber brukeren om å skrive et tall, som tilsvarer valgt planet i lista
    planetnummer = input("\n Velg en planet ved å skrive et tall: ")
    planetnummer = int(planetnummer) - 1

    # Gir tilbakemelding mo hvilken planet som er valgt
    valgt_planet = planeter[planetnummer]
    print(f"\n Du har valgt {valgt_planet}")

    # Ber om brukerens vekt, som umiddelbart gjøres om til float
    din_vekt = float(input("\n Hva er din vekt på jorden?"))

    # Utregninger
    jordens_tyngdekraft = tyngdekraft[2]
    din_masse = din_vekt / jordens_tyngdekraft
    din_vekt_på_planet = din_masse * tyngdekraft[planetnummer]

    # Utskrift av brukers vekt på valgt planet
    print(f"Din vekt på planeten {valgt_planet} er {round(din_vekt_på_planet, 2)} kg.")

    # Brukeren spørres om hen vil prøve igjen
    en_gang_til = input("Vil du prøve igjen? Y/N ")

    # en_gang_til.upper() == 'Y' sammenligner brukerens input med 'Y'. Med andre ord, er det brukeren skrev inn identisk med 'Y'?
    # Dersom det brukeren skrev inn er identisk med 'Y' blir uttrykket True, som igjen blir ny verdi for variabelen kjør
    # Er det ikke identisk med 'Y' vil uttrykket, og dermed ny verdi for kjør, bli False
    # Dersom kjør blir satt til False vil løkka avsluttes, se linje 11 og 12!
    kjør = en_gang_til.upper() == 'Y'

