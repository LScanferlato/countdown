from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Data di riferimento
    target_date = datetime(2030, 12, 1)
    max_target_date = datetime(2038, 8, 1)
    # Data attuale
    current_date = datetime.now()
    # Calcolo dei giorni rimanenti
    days_remaining = (target_date - current_date).days
    maxdays_remaining = (max_target_date - current_date).days
    # Passa i dati al template
    return render_template('index.html', days_remaining=days_remaining, maxdays_remaining=maxdays_remaining)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
