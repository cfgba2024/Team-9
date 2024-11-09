from flask import Flask, jsonify
import mysql.connector
import ConexionesDB.py

app = Flask(__name__)

# Configura los parámetros de conexión
DB_CONFIG = {
    'host': '192.168.195.223',  # o 'localhost' si es local
    'user': 'root',
    'password': '1898',
    'database': 'escolares'
}

@app.route("/")
def get_publicaciones():
    # Conectar a la base de datos
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)  # Cursor con diccionario para mejor lectura

    try:
        # Realizar una consulta
        cursor.execute("SELECT * FROM Publicacion")  # Cambia 'publicaciones' por el nombre de tu tabla
        results = cursor.fetchall()  # Obtener todos los resultados

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()

@app.route("/actividad/metricas/<id>")
def devolver_metricas():
    # Conectar a la base de datos
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)  # Cursor con diccionario para mejor lectura

    try:
        # Realizar una consulta
        cursor.execute("SELECT * FROM Metrica WHERE ID_Metrica in (SELECT ID_Metrica FROM Medica_Actividad WHERE ID_Actividad = %s", id)  # Cambia 'publicaciones' por el nombre de tu tabla
        results = cursor.fetchall()  # Obtener todos los resultados

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()

@app.route("/registers/schools/<id>")
def info_formulario_registro(id):
    # Conectar a la base de datos
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)  # Cursor con diccionario para mejor lectura

    try:
        # Realizar una consulta
        cursor.execute("SELECT * FROM Actividad WHERE ID_colegio = %s", id)  # Cambia 'publicaciones' por el nombre de tu tabla
        results = cursor.fetchall()
        

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()

@app.route("/schools/activities/<id>")
def actividades_de_la_escuela(id):
        # Conectar a la base de datos
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)  # Cursor con diccionario para mejor lectura

    try:
        # Realizar una consulta
        cursor.execute("SELECT * FROM Colegio")  # Cambia 'publicaciones' por el nombre de tu tabla
        results = cursor.fetchall()
        

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()



if __name__ == "__main__":
    app.run(debug=True, port=5000)