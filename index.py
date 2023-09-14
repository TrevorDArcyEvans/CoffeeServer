#!/usr/bin/env python

import RPi.GPIO as GPIO
from datetime import datetime, date
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

OrderStatus = "Now taking orders"

@app.route("/")
def index():
  return app.send_static_file('index.html')

@app.route("/order")
def order():
  global OrderStatus
  OrderStatus = "Requested"
  GPIO.output(15, GPIO.HIGH)
  return OrderStatus

@app.route("/received")
def received():
  global OrderStatus
  OrderStatus = "Now taking orders"
  GPIO.output(15, GPIO.LOW)
  return OrderStatus

@app.route("/acknowledged")
def acknowledged():
  global OrderStatus
  OrderStatus = "Acknowledged"
  return OrderStatus

@app.route("/status")
def status():
  global OrderStatus
  return OrderStatus


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)

# turn off light
GPIO.output(15, GPIO.LOW)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded = True)

