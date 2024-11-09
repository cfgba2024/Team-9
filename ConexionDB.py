import os
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB")):
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

        
#     gets
    def getPublicacion(self, ID):
        query = 'select * from Publicacion where ID_Publicacion = %s'
        params = (ID, )

        return self.select_query(query, params)

    def getUsuario(self, ID):
        query = 'select * from Usuario where ID_Usuario = %s'
        params = (ID, )

        return self.select_query(query, params)
          
    def getMetrica(self, ID):
        query = 'select * from Metrica where ID_Metrica = %s'
        params = (ID, )

        return self.select_query(query, params)

    def getActividad(self, ID):
        query = 'select * from Actividad where ID_Actividad = %s'
        params = (ID, )

        return self.select_query(query, params)

    def getColegio(self, ID):
        query = 'select * from Colegio where ID_Colegio = %s'
        params = (ID, )

        return self.select_query(query, params)

    def getEtiqueta(self, ID):
        query = 'select * from Etiqueta where ID_Etiqueta = %s'
        params = (ID, )

        return self.select_query(query, params)

        
    def etiquetas_por_publicacion(self, ID_Publicacion):
        query = 'select * from Etiqueta E where exists (select 1 from Publicacion-Etiqueta PE where ID_Publicacion = 1 and PE.ID_Etiqueta = E.ID_Etiqueta and E.ID_Publicacion = %s)'
        params = (ID_Publicacion, )

        return self.select_query(query, params)
          

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

    def select_query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.connection.commit()
            return self.cursor.fetchall() 
        except Error as e:
            print(f"Error: {e}")
            return 0

# Ejemplo
if __name__ == "__main__":
#     db = Database(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"))
    db = Database()

    # Connect to the database
    db.connect()

    # Example of executing an INSERT query
#     db.nueva_publicacion(1, "hola", "mundo")
#     db.nuevo_colegio("Escuela 2")



    db.close()
