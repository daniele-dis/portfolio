In questo progetto non ho fatto altro che implementare un gestore di password.
Abbiamo 3 file principali:
-main
-Credenziali
-psswGestorePss

Il primo permette l'esecuzione del flusso di esecuzione, nel secondo ci sono le credenziali che ci permetteranno di essere riconosciuto dal sistema, quindi sono credenziali pre-impostate come Username: XXXX e Password: 1234, ma che possono essere editate a proprio piacimento prima dell'esecuzione del programma stesso.
Se l'autenticazione va a buon fine, il file psswGestorePss permette di conservare, visualizzare ed eliminare password inserite dall'utente.
infine, questi file contenenti informazioni sensibili vengono poi decifrati e cifrati prima dell'avvio del programma e dopo la sua fine, in modo che quelle informazioni non siano immediatamente leggibili.