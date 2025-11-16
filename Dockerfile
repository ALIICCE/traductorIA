FROM python:3.10-slim

# crear carpeta de la app
WORKDIR /app

# copiar archivos
COPY . .

# instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# exponer puerto de streamlit
EXPOSE 10000

# ejecutar streamlit
CMD ["streamlit", "run", "buscale.py", "--server.port=10000", "--server.address=0.0.0.0"]
