# Python
FROM python:3.8

# Configura las variables de entorno
ENV API_URL='https://api.coingecko.com/api/v3/exchanges/list' \
    REDSHIFT_DB='data-engineer-database' \
    REDSHIFT_USER='gonzalo_lemos87_coderhouse' \
    REDSHIFT_PASSWORD='hQ79Q7LVgN' \
    REDSHIFT_HOST='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com' \
    REDSHIFT_PORT='5439' \
    TABLE_NAME='exchange_data'

# Instala las dependencias desde requirements.txt
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Copia el script al contenedor
COPY Script_Cripto_Exchanges.py /

# Ejecuta el script cuando se inicie el contenedor
CMD ["python", "/Script_Cripto_Exchanges.py"]
