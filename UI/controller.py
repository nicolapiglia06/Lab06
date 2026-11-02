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
