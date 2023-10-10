import mysql.connector

class MySQLDatabase:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'kioskopop',
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")
