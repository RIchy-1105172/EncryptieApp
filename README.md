# Wachtwoord Encryptie

Een simpele command line app om wachtwoorden te versleutelen en ontsleutelen. Hier word gebruik gemaakt van een symmetrische encryptie. Ik heb hiervoor Python gebruikt met behulp van cryptography library.

## Hoe werkt het
Na het starten van de app krijg je een keuze menu. Menu bestaat uit 4 keuzes:
1. sleutel genereren
2. wachtwoord versleutelen
3. wachtwoord ontsleutelen
4. sluiten

Met behulp van optie 2 kan je optie 3 gebruiken. Mocht je al een Encrypted wachtwoord hebben kan je optie 3 gebruiken om het te ontsleutelen.

## library
Ik heb gebruik gemaakt van de library cryptography, met de schema Fernet.
Ik heb deze library gebruikt omdat ik hiermee eenvoudig op een symmetrische manier tekst kan versleutelen en ontsleutelen.
Fernet maakt gebruik van een AES. Het regelt automatisch zaken als initialisatievectoren (IV’s), padding en HMAC-controle, waardoor fouten moeilijker te maken zijn.

## Hoe wordt het gemaakt
De symmetrische sleutel wordt één keer aangemaakt met `Fernet.generate_key` en key.key`. Wanneer de app start wordt deze sleutel ingeladen en gebruikt voor zowel versleuteling als ontsleuteling.

## Reflectie
De app voldoet aan alle Kerchhoff eisen. Dit betekent dat de veiligheid van het sleutelen van tekst mag afhangen van de geheimhouding.
Vandaar dat er ook gebruik is gemaakt van Fernet AES. Daarmee is de applicatie veilig zolang de sleutel privé blijft en niet gedeeld wordt.

## Installatie
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt