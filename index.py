import os
from dotenv import load_dotenv

# Cargar el archivo .env adecuado
# Cambia '.env' por '.env.dev' o '.env.pro' según el entorno que necesites
load_dotenv('.env.dev')  # Descomentar para usar el entorno de desarrollo
#load_dotenv('.env.pro')  # Descomentar para usar el entorno de producción

# Leer las variables de entorno
user_name = os.getenv('USER_NAME')
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
database_url = os.getenv('DATABASE_URL')



# Imprimir las variables para verificar
print(f'USER_NAME: {user_name}')
print(f'API_KEY: {api_key}')
print(f'EMAIL: {email}')
print(f'DATABASE_URL: {database_url}')

