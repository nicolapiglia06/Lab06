import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        """
        Gestisce il click sul pulsante 'Mostra' per caricare tutti gli strumenti dal database.
        """
        # 1. Richiede al modello la lista completa degli strumenti presenti nel DB
        strumenti = self._model.get_strumenti()

        # 2. Svuota la ListView della View per evitare duplicati
        self._view.lista_strumenti.controls.clear()

        # 3. Gestione dell'errore di connessione (se il model restituisce None)
        if strumenti is None:
            self._view.show_alert("Errore durante la connessione al database!")
            self._view.update()
            return

        # 4. Se non ci sono strumenti o se la lista è stata popolata
        if not strumenti:
            self._view.lista_strumenti.controls.append(
                ft.Text("Nessuno strumento presente nel deposito.")
            )
        else:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        # 5. Aggiorna l'interfaccia grafica per mostrare il risultato
        self._view.update()
    def cerca_strumenti (self,e):
        tipo = self._view.input_tipo_strumento.value
        if not tipo or not tipo.strip():
            self._view.show_alert("Inserisci un tipo di strumento valido per la ricerca!")
            self._view.update()
            return
        tipo_pulito = tipo.strip()
        strumenti = self._model.cerca_strumenti_per_tipo(tipo_pulito)
        self._view.lista_strumenti_ricerca.controls.clear()
        if strumenti is None:
            self._view.show_alert("errore")
            self._view.update()
            return
        if not strumenti:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(f"Nessuno strumento trovato per il tipo '{tipo_pulito}'.")
            )
        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))
        self._view.update()
