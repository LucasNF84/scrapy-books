import os
from dotenv import load_dotenv

load_dotenv()

print("🔹 PostgreSQL Configuración:")
print("Host:", os.getenv("POSTGRES_HOST"))
print("DB:", os.getenv("POSTGRES_DB"))
print("User:", os.getenv("POSTGRES_USER"))
print("Password:", os.getenv("POSTGRES_PASSWORD"))  # 🚨 Ver si se imprime la contraseña
print("Port:", os.getenv("POSTGRES_PORT"))