# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY index.html templates/index.html
# Espone la porta 5000
EXPOSE 5000

# Comando per avviare l'app
CMD ["python", "app.py"]
