from werkzeug.security import generate_password_hash, check_password_hash

password = 'luis'

# Generar un hash seguro de la contraseña
hashed_password = generate_password_hash(password)
print(hashed_password)

# Verificar la contraseña
print(check_password_hash(hashed_password, password))  # Esto debería imprimir True
