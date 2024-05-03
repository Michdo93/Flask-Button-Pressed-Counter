from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Globale Variable für den Zähler
counter = 0

# Globale Variable für den Status des Buttons
button_pressed = False

# Flask-Routen definieren
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket-Routen definieren
@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    global button_pressed
    global counter

    data = request.json
    button_pressed = data['button_pressed']
    
    while True:
        if button_pressed:
            counter += 1
            print("Counter:", counter)
            time.sleep(1)  # Kurze Verzögerung, um die Ausgabe lesbar zu machen
        else:
            time.sleep(0.1)  # Kurze Verzögerung, um die CPU nicht zu überlasten

    return '', 204

if __name__ == '__main__':
    # Flask-App starten
    app.run(debug=True)
