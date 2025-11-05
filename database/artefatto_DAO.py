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
            query = "SELECT * FROM artefatto"
            cursor.execute(query)
            lista_epoche = []
            for row in cursor.fetchall():
                artefatto = Artefatto(int(row[0]), row[1], row[2], row[3], row[4])
                lista_epoche.append(artefatto.epoca)
            connection.close()
            return lista_epoche

    def lista_artefatti_filtrati(self, museo, epoca):
        connection = ConnessioneDB.get_connection()
        with connection.cursor() as cursor:
            if not museo == "Nessun filtro":
                get_museo_id_query = "SELECT id FROM museo WHERE nome = %s"
                cursor.execute(get_museo_id_query, (museo, ))
                id = cursor.fetchone()[0]
                if not epoca == "Nessun filtro":
                    get_artefatti_query = "SELECT * FROM artefatto WHERE id_museo = %s AND epoca = %s;"
                    cursor.execute(get_artefatti_query, (id, epoca))
                else:
                    get_artefatti_query = "SELECT * FROM artefatto WHERE id_museo = %s"
                    cursor.execute(get_artefatti_query, (id, ))
            else:
                if not epoca == "Nessun filtro":
                    get_artefatti_query = "SELECT * FROM artefatto WHERE epoca = %s;"
                    cursor.execute(get_artefatti_query, (epoca, ))
                else:
                    get_artefatti_query = "SELECT * FROM artefatto"
                    cursor.execute(get_artefatti_query)

            lista_artefatti = []
            for row in cursor.fetchall():
                artefatto = Artefatto(int(row[0]), row[1], row[2], row[3], row[4])
                lista_artefatti.append(artefatto)
            connection.close()
            return lista_artefatti
