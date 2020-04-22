#!/usr/bin/python

from flask import Flask
import RPi.GPIO as GPIO

MOTORES = {"uno": 37, "dos": 36}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTORES["uno"], GPIO.OUT)
GPIO.setup(MOTORES["dos"], GPIO.OUT)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def api_root():
    return ""

@app.route('/motor/<numero>/lectura/', methods=["GET"])
def api_motores_lectura():

    return GPIO.input(MOTORES[numeoro])

@app.route('/motor/<numero>/encender/', methods=["GET"])
def api_motores_control(numero):

    GPIO.output(MOTORES[numero], GPIO.LOW)

    return ""

@app.route('/motor/<numero>/apagar/', methods=["GET"])
def api_motores_control2(numero):

    GPIO.output(MOTORES[numero], GPIO.HIGH)

    return ""

@app.route('/sensor/dht11/lectura/', methods=["GET"])
def api_sensores_lectura():

    file = open("lecturaDHT11.json","r")

    return file.read()

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
