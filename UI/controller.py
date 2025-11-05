import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self, tipo):
        if tipo == "Museo":
            self._view.dropdown_museo.options.append(ft.dropdown.Option("Nessun filtro"))
            for museo in self._model.get_musei():
                self._view.dropdown_museo.options.append(ft.dropdown.Option(museo))
        elif tipo == "Epoca":
            self._view.dropdown_epoca.options.append(ft.dropdown.Option("Nessun filtro"))
            epoche = set(self._model.get_epoche())
            for epoca in epoche:
                self._view.dropdown_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.update()

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, museo, epoca):
        lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)
