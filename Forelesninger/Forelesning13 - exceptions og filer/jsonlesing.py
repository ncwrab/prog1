# For å få tilgang til ferdiglagde json-funksjonalitet må vi importere modulen/biblioteket 'json'

import json

# Vi lager dictionary-er (i en liste).
planeter = [{'name': "Merkur", 'tyngdekraft' : 3.7},
            {'name': 'Venus', 'tyngdekraft': 8.87},
            {'name': 'Jorden', 'tyngdekraft': 9.807}
]

# Åpner en fil 'planeter.json' og spesifiserer at vi vil skrive til den med "w".
# ved å benytte dump() kan vi skrive vår dictionary til json-filen
# 'indent=4' er ikke nødvendig å ha med, men dette vil formatere teksten i fila slik at den (muligens) blir mer lesbar for oss.
with open("planeter.json", "w") as utfil:
    json.dump(planeter, utfil, indent=4)
