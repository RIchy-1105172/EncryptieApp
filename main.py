from cryptography.fernet import Fernet
from pathlib import Path

KEY_PATH = Path("key.key")

def keymaker():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)

def keyget():
    if not KEY_PATH.is_file():
        return None
    with open(KEY_PATH, "rb") as f:
        return f.read()

def encryption():
    keyg = keyget()
    if not keyg:
        return
    tekst = input("Enter your password: ")
    f = Fernet(keyg)
    try:
        token = f.encrypt(tekst.encode("utf-8"))
        print("\nENCRYPTED WACHTWOORD")
        print(token.decode("utf-8"))
    except Exception as e:
        print("iets ging mis bij de encryptie:", e)

def decryption():
    key = keyget()
    if not key:
        return
    token = input("Encryption text:").strip()
    f = Fernet(key)
    try:
        plain = f.decrypt(token.encode("utf-8"))
        print("\nONTSLEUTELD WACHTWOOR:D")
        print(plain.decode("utf-8"))
    except Exception as e:
        print("Fout! kan niet sleutelen", e)

def menu():
    print("\nWACHTWOORD ENCRYPTION")
    print("1) maak key)")
    print("2) wachtwoord versluitelen")
    print("3) wachtwoord ontsleutelen")
    print("4) sluiten")
    keuze = input("maak een keuze met behulp van een cijfer").strip()
    return keuze

if __name__ == "__main__":
    while True:
        k = menu()
        if k == "1":
            keymaker()
        elif k == "2":
            encryption()
        elif k == "3":
            decryption()
        elif k == "4" or k == "":
            print("gelukt")
            break
        else:
            print("maak een keuze met behulp van een cijfer")
