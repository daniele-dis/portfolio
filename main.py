#hello = "Ciao, questa è una prova di Python"
#print(hello)
import getpass
import pwinput
from dotenv import load_dotenv
from cryptography.fernet import Fernet, InvalidToken
import os
import base64

#---------------------AREA DI DEFINIZIOEN METODI PER LE PASSWORD E VARIABILI--------------------------

HEADER = b"CRYPT:"
verde = "\033[32m"
giallo = "\033[33m"
reset = reset = "\033[0m"

def carica_credenziali(percorso="Credenziali.txt"):
    credenziali = {}
    with open(percorso, "r", encoding="utf-8-sig") as f:
        for line in f:
            if ":" in line:
                line = line.strip()  # Rimuove eventuali spazi extra e ritorni a capo
                nome, password = line.split(":", 1)
                credenziali[nome] = password
    return credenziali

#========== GENERAZIONE E LETTURA CHIAVE ==========
def genera_chiave():
    if not os.path.exists("chiave.key"):
        with open("chiave.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
        print("[+] Chiave generata.")
    else:
        print("[✓] Chiave già esistente.")

def carica_chiave():
    with open("chiave.key", "rb") as key_file:
        return key_file.read()
    
    # ========== CIFRA E DECIFRA FILE ==========

def cifra_file(nome_file):
    try:
        with open(nome_file, "rb") as file:
            contenuto = file.read()

        f = Fernet(carica_chiave())
        contenuto_cifrato = f.encrypt(contenuto)

        with open(nome_file, "wb") as file:
            file.write(contenuto_cifrato)

        print(f"[✓] {nome_file} cifrato.")
    except Exception as e:
        print(f"[x] Errore durante la cifratura di {nome_file}: {e}")

def decifra_file(nome_file):
    try:
        with open(nome_file, "rb") as file:
            contenuto = file.read()

        f = Fernet(carica_chiave())
        contenuto_decifrato = f.decrypt(contenuto)

        with open(nome_file, "wb") as file:
            file.write(contenuto_decifrato)

        print(f"[✓] {nome_file} decifrato.")
    except InvalidToken:
        print(f"[!] {nome_file} è già in chiaro o token non valido.")
    except Exception as e:
        print(f"[x] Errore durante la decifratura di {nome_file}: {e}")

#-------------FINE FUNZIONI PER LA CHIAVE E LA CIFAATURA

#----------INIZIO GESTIONE NOME E PASSWORD

def inserisciNome():
    nome = input("Inserisci il tuo nome: ")
    print("Ciao, ",nome)
    return nome

#definizione di una funzione che controlla il nome inserito

def controlloNome(nome):
    tentativi = 3
    credenziali = nomi = carica_credenziali()

    while tentativi > 0:
        if nome in credenziali:
            print("Bentornato Admin!\n")
            return True
        else:
            tentativi = tentativi -1
            if tentativi > 0:
                print("Tentativi rimasti = ", tentativi) 
                print("Non sei l'admin, accesso negato !")
                nome = inserisciNome()
            else:
                print("Numero Tentativi Esauriti, Non Hai Accesso")
                quit()
                break


    print("Numero Tentativi Esauriti, Non Hai Accesso")
    quit()

#definisco un metodo che mi permette di inserire la password e di richiamarlo più volte
def inserisciPassw():
        password = pwinput.pwinput(prompt="Inserisci la tua password admin: ", mask='*')
        return password

def controlloPassw(password):
        tentativipass = 3
        credenziali = carica_credenziali()  # Carica le credenziali decifrate

        while tentativipass > 0:
            # Rimuovi spazi extra sia dalla password inserita che da quella salvata
            password_input = password.strip()  # Rimuove gli spazi dalla password inserita
            if password_input in credenziali.values():
                print("Accesso Autorizzato.\n")
                return True
            else:
                tentativipass -= 1
                if tentativipass > 0:
                    print("Password errata!")
                    print("Tentativi rimasti:", tentativipass)
                    password = inserisciPassw()
                else:
                    print("Accesso Negato, numero di tentativi esaurito\n")
                    quit()

        print("Numero Tentativi Esauriti, Non Hai Accesso")
        quit()

#---------------FUNZIONE CHE MI PERMETTE DI INSERIRE UNA NUOVA PASSOWRD, NEL FILE DEDICATO
def InserisciNewPassw():
    # Non uso gli asterischi perché qui voglio visualizzare la password
    password = input("Inserisci una nuova password al tuo gestore password: \n")

    # Verifica che la password non sia solo spazi
    while password.isspace() or password == "":
        print("Password non valida! Non puoi inserire solo spazi.")
        password = input("Inserisci una nuova password al tuo gestore password: \n")
    
    # A questo punto la password è valida, la salviamo nel file
    with open("psswGestorePss.txt", "a") as file_uno:
        file_uno.write(password + "\n")

    print("Password inserita con successo!\n")

#----------FUNZIONE CHE MI PERMETTE DI VISUALIZZARE QUELLE PASSWORD INSERITE
def ViewAllPassw() :

    var_lettura = open("psswGestorePss.txt", "r").read()
    print(f"{verde}Password: {giallo}{var_lettura}{reset}")
    exit

#------------FUNZIONE CHE MI RI-STAMPA LE PASSWORD SALVATE E MI CHIEDE QUALE VOGLIO ELIMIANARE
def DeleteAPassw():
    # Leggi tutte le righe del file come lista
    with open("psswGestorePss.txt", "r") as f:
        righe = [line.strip() for line in f]  # rimuove i \n
    
    # Stampa tutte le password

    for riga in righe:
         print(f"{giallo}{riga}{reset}")

    print("\n")
    var_remove = input("Inserisci la Password da rimuovere: ")

    if var_remove in righe:
        righe.remove(var_remove)  # funziona perché righe è una lista
        with open("psswGestorePss.txt", "w") as f:
            for riga in righe:
                f.write(riga + "\n")
        print("Password eliminata.\n")
    else:
        print("Password non trovata.\n")

    exit

# Esempio di utilizzo
    #genera_chiave()  # Una sola volta per generare la chiave
    #cifra_file("psswGestorePss.txt")  # Cifra il file
    #decifra_file("psswGestorePss.txt.cif")  # Decripta il file quando serve


#--------------------------------------------------------------------
#MAIN

genera_chiave()  # Una sola volta per generare la chiave
decifra_file("Credenziali.txt")
decifra_file("PsswGestorePss.txt")

nomeIns = inserisciNome()
controlloNome(nomeIns)

passwins = inserisciPassw()
controlloPassw(passwins)

print("1.per inserire una nuova password. \n" \
"2. per visualizzare le tue password. \n" \
"3. per eliminare una password esistente. \n" \
"4. per uscire senza effettuare operazioni \n ")
scelta = input("Quale Operazione Vuoi Svolgere?: ")
#scelta = int(scelta)    #altrimenti mi crea problemi di incompatib tra string e interi
while True:
    scelta = input("Inserisci un numero intero: ")
    if scelta.isdigit():
        scelta = int(scelta)
        break
    else:
        print("Valore non valido. Inserisci un numero intero.\n")

while scelta < 5 :
    match scelta:
        case 1:
            print("Vuoi inserire una nuova password.")
            InserisciNewPassw()

        case 2:
            print("Vuoi visualizzare le tue password, eccole.")
            ViewAllPassw()

        case 3:
            print("Vuoi eliminare una password esistente.")
            DeleteAPassw()

        case 4:
            cifra_file("Credenziali.txt")
            cifra_file("psswGestorePss.txt")
            print("Uscita dal programma in corso...\n")
            quit()
      
    print("1.per inserire una nuova password. \n" \
    "2. per visualizzare le tue password. \n" \
    "3. per eliminare una password esistente. \n" \
    "4. per uscire senza effettuare operazioni \n ")
    scelta = input("Quale Operazione Vuoi Svolgere?: ")
    scelta = int(scelta)

quit()
