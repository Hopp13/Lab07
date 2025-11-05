from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def lista_epoche(self):
        connection = ConnessioneDB.get_connection()
        with connection.cursor() as cursor:
            query = "SELECT epoca FROM artefatto"
            cursor.execute(query)
            lista_musei = []
            for row in cursor.fetchall():
                lista_musei.append(row[0])
            return lista_musei

    def lista_artefatti_filtrati(self, museo, epoca):
        connection = ConnessioneDB.get_connection()
        with connection.cursor() as cursor:
            get_museo_id_query = "SELECT id FROM museo WHERE nome = %s"
            cursor.execute(get_museo_id_query, (museo, ))
            id = cursor.fetchall()
            get_artefatti_query = "SELECT * FROM artefatto WHERE id = %s, epoca = %s"
            cursor.execute(get_artefatti_query, (id, epoca))
            lista_artefatti = []
            for row in cursor.fetchall():
                lista_artefatti.append((row[0], row[1], row[2], row[3]))
            return lista_artefatti
