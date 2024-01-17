import requests
import pandas as pd
from sqlalchemy import create_engine, inspect

# Configuración de la API y Redshift
api_url = 'https://api.coingecko.com/api/v3/exchanges/list'
redshift_config = {
    'dbname': 'data-engineer-database',
    'user': 'gonzalo_lemos87_coderhouse',
    'password': 'hQ79Q7LVgN',
    'host': 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
    'port': '5439'
}
table_name = 'exchange_data'

# Obtener datos de la API
response = requests.get(api_url)
exchange_data = response.json()

# Crear un DataFrame con los datos
df = pd.DataFrame(exchange_data)

# Conectar a Redshift utilizando SQLAlchemy
engine = create_engine(f"postgresql+psycopg2://{redshift_config['user']}:{redshift_config['password']}@{redshift_config['host']}:{redshift_config['port']}/{redshift_config['dbname']}")

# Verificar si la tabla ya existe en la base de datos
inspector = inspect(engine)
if not inspector.has_table(table_name):
    # Si la tabla no existe, la creamos
    df.to_sql(table_name, engine, index=False)
else:
    # Si la tabla ya existe, simplemente insertamos los datos
    df.to_sql(table_name, engine, if_exists='append', index=False)

# Cerrar la conexión
engine.dispose()
