from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from datetime import datetime


password = '12345'

# Generar un hash seguro de la contraseña
hashed_password = generate_password_hash(password)
print(hashed_password)

# Verificar la contraseña
print(check_password_hash(hashed_password, password))  # Esto debería imprimir True




# Configuración de la conexión a la base de datos
""" MYSQL_HOST = '10.39.4.200'
MYSQL_USER = 'userdml23'
MYSQL_PASSWORD = 'Beex2023%'
MYSQL_DB = 'kiosk'
 """
""" try:
    # Intentar establecer una conexión
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    if connection.is_connected():
        print("¡Conexión exitosa!")

    # Cerrar la conexión
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {str(e)}") """




current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]

print("La fecha actual es:", formatted_date)
