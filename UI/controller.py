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
                self._view.dropdown_museo.options.append(ft.dropdown.Option(museo.nome))
        elif tipo == "Epoca":
            self._view.dropdown_epoca.options.append(ft.dropdown.Option("Nessun filtro"))
            epoche = set(self._model.get_epoche())
            for epoca in epoche:
                self._view.dropdown_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.update()

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        self.museo_selezionato = self._view.dropdown_museo.value
        self.epoca_selezionata = self._view.dropdown_epoca.value
        lista_artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        self._view.listview_artefatti.controls.clear()
        for artefatto in lista_artefatti:
            self._view.listview_artefatti.controls.append(ft.Text(value = artefatto))
        if len(self._view.listview_artefatti.controls) == 0:
            self._view.show_alert("Nessun artefatto trovato")
        self._view.update()
