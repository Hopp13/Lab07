from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def lista_musei(self):
        connection = ConnessioneDB.get_connection()
        with connection.cursor() as cursor:
            query = "SELECT nome FROM museo"
            cursor.execute(query)
            lista_musei = []
            for row in cursor.fetchall():
                lista_musei.append(row[0])
            connection.close()
            return lista_musei
