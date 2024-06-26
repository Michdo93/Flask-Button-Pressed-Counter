# Flask-Button-Pressed-Counter
As long as a button in the HTML page is held down, a counter is incremented in the command line. The application uses Python and Flask for the backend and HTML and JS in the frontend.

## Pre-Installation

Please make sure, that `Flask` is installed:

```
python -m pip install flask
```

## Usage

You can run it with:

```
python flask_example.py
```

As example you will receive:


```
python .\flask_test.py
 * Serving Flask app 'flask_test'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 143-323-067
Counter: 1
Counter: 2
Counter: 3
Counter: 4
Counter: 5
Counter: 6
Counter: 7
Counter: 8
Counter: 9
Counter: 10
....
```

Important is that if you release the button, the counter will not be incremented. If you pressed the button again the counter will incremented as long as you hold the button pressed.
