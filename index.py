#!/usr/bin/env python

import RPi.GPIO as GPIO
from datetime import datetime, date
from flask import Flask, session

app = Flask(__name__, static_url_path='', static_folder='')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
  return app.send_static_file('index.html')

@app.route("/order")
def order():
  session["OrderReceived"] = datetime.now()
  GPIO.output(15, GPIO.HIGH)
  return session["OrderReceived"].__str__()

@app.route("/received")
def received():
  session["OrderReceived"] = None
  GPIO.output(15, GPIO.LOW)
  return None.__str__()

@app.route("/status")
def status():
  return session["OrderReceived"].__str__() if ("OrderReceived" in session) else None


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)

# turn off light
GPIO.output(15, GPIO.LOW)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded = True)

