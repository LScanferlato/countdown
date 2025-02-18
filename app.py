from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Data di riferimento
    target_date = datetime(2030, 11, 30)
    # Data attuale
    current_date = datetime.now()
    # Calcolo dei giorni rimanenti
    days_remaining = (target_date - current_date).days
    return f"<h1>Giorni rimanenti al 30/11/2030: {days_remaining}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
