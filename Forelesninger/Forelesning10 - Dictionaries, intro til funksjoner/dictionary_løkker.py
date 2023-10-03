brettspill = {
    'tittel' : 'Dixit',
    'spilletid' : 30,
    'aldersgrense' : 8,
}

# Itererer gjennom og skriver ut nøklene/keys i dictionaryen med en for-løkke
for key in brettspill:
    print(f"{key} ")

# Itererer gjennom og skriver ut verdiene/values i dictionaryen med en for-løkke
for value in brettspill.values():
    print(value)

# Itererer gjennom og skriver ut både nøkkel/key OG verdi/value som fins i dictionaryen med en for-løkke
for key, value in brettspill.items():
    print(f"{key} - {value}")
