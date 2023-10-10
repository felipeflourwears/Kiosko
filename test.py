from database.class_connection import MySQLDatabase

if __name__ == "__main__":
    db = MySQLDatabase()
    
    db.connect()

    # Consulta SELECT de prueba en la tabla "foodMenu"
    select_query = "SELECT * FROM foodMenu"

    result = db.execute_query(select_query)

    # Recorre los resultados y muestra los datos
    for row in result:
        print("ID:", row[0])
        print("Nombre de la comida:", row[1])
        print("Precio:", row[2])
        print("URL de la imagen:", row[3])
        print("Descripción:", row[4])
        print("Disponible:", "Sí" if row[5] == 1 else "No")
        print("ID de la categoría:", row[6])
        print()

    db.close()
