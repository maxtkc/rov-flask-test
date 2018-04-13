from flask import Flask
import serial
app = Flask(__name__)
ser = serial.Serial(4)

@app.route("/<str>")
def hello(str):
    ser.write(str) # send the command
    return myArduinoCommand + " " + str(ser.outWaiting()) + " " + str(ser.inWaiting())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
