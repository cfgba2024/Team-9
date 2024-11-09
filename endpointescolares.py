from flask import Flask, jsonify
import mysql.connector
import ConexionDB
import os

app = Flask(__name__)

# Configura los parámetros de conexión


@app.route("/")
def get_publicaciones():
    # Conectar a la base de datos
    db.connect()

    try:
        # Realizar una consulta
        results = ConexionDB.select_query("SELECT * FROM Publicacion")
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        db.close()

@app.route("/actividad/metricas/<id>")
def devolver_metricas():
    # Conectar a la base de datos
    db.connect()

    try:
        # Realizar una consulta
        results = ConexionDB.select_query("SELECT * FROM Metrica WHERE ID_Metrica in (SELECT ID_Metrica FROM Medica_Actividad WHERE ID_Actividad = %s", id)  # Cambia 'publicaciones' por el nombre de tu tabla
         # Obtener todos los resultados

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        db.close()

@app.route("/registers/schools/<id>")
def info_formulario_registro(id):
    # Conectar a la base de datos
    db.connect()  # Cursor con diccionario para mejor lectura

    try:
        # Realizar una consulta
        results = ConexionDB.select_query("select * from ")
        

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        db.close()

@app.route("/schools/activities/<id>")#devuelve la actividad conel id
def actividades_de_la_escuela(id):
    
    db.connect()

    try:
        # Realizar una consulta
        
        results = ConexionDB.select_query("select * from actividad where id = %s", id)

        # Devuelve los resultados como un JSON
        return jsonify(results)
    
    except mysql.connector.Error as err:
        # Manejo de errores
        return jsonify({"error": str(err)}), 500
    
    finally:
        # Cerrar la conexión
        db.close()



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    db = ConexionDB.Database(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"))

    # Connect to the database
    