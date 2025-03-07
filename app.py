from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Data di riferimento
    target_date = datetime(2030, 12, 1)
    max_target_date = datetime(2030, 12, 1)
    # Data attuale
    current_date = datetime.now()
    # Calcolo dei giorni rimanenti
    days_remaining = (target_date - current_date).days
    maxdays_remaining = (max_target_date - current_date).days
    # Formatta il testo di ritorno su due righe
    return (
        f"<h1>Giorni rimanenti al {target_date}: {days_remaining}</h1>\n"
        f"<h2>Giorni massimi rimanenti al {max_target_date}: {maxdays_remaining}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
