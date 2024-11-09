import os
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Establish the connection to the database
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print(f"Connected to MySQL database: {self.database}")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
            return None

    def close(self):
        # Close the connection and cursor
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
 
    def nuevo_registro(self, ID_Actividad_Metrica:str, Valor:str, Fecha):
        query = 'Insert Into Registro (ID_Actividad-Metrica, Valor, Fecha) values (%s, %s, %s)'
        params = (ID_Actividad_Metrica, Valor, Fecha)

        rows_affected = self.execute_query(query, params)
        return rows_affected

    def nuevo_usuario(self, ID_Colegio:str, Nombre:str, Apellido, Mail):
        query = 'Insert Into Usuario (ID_Colegio, Nombre, Apellido, mail) values (%s, %s, %s, %s)'
        params = (ID_Colegio, Nombre, Apellido, Mail)

        rows_affected = self.execute_query(query, params)
        return rows_affected
 
    def nueva_actividad(self, Nombre:str):
        query = 'Insert Into Actividad (Descr) values (%s)'
        params = (Nombre, )

        rows_affected = self.execute_query(query, params)
        return rows_affected
 
    def nuevo_colegio(self, Nombre:str):
        query = 'Insert Into Colegio (Descr) values (%s)'
        params = (Nombre, )

        rows_affected = self.execute_query(query, params)
        return rows_affected
 
    def nueva_metrica(self, Descripcion:str):
        query = 'Insert Into Metrica (Descr) values (%s)'
        params = (Descripcion, )

        rows_affected = self.execute_query(query, params)
        return rows_affected

    def nueva_publicacion(self, Usuario:str, Titulo:str, Cuerpo:str):
        query = 'Insert Into Publicacion (ID_Usuario, Titulo, Cuerpo) values (%s, %s, %s)'
        params = (Usuario, Titulo, Cuerpo)

        rows_affected = self.execute_query(query, params)
        return rows_affected


    def execute_query(self, query, data=None):
        """
        Executes a query (INSERT, UPDATE, DELETE) with or without parameters.
        
        :param query: SQL query string.
        :param data: Tuple or list of data to bind to the query.
        :return: Number of affected rows.
        """
        try:
            self.cursor.execute(query, data)
            self.connection.commit()
            return self.cursor.rowcount  # Number of affected rows
        except Error as e:
            print(f"Error: {e}")
            return 0

# Ejemplo
if __name__ == "__main__":
    db = Database(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"))

    # Connect to the database
    db.connect()

    # Example of executing an INSERT query
#     db.nueva_publicacion(1, "hola", "mundo")
    db.nuevo_colegio("Escuela 2")



    db.close()
