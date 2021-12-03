'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
leftFwd = 7
leftBckwd = 8
rightFwd= 10
rightBckwd = 12

# Define pins as output
GPIO.setup(leftFwd, GPIO.OUT)   
GPIO.setup(leftBckwd, GPIO.OUT) 
GPIO.setup(rightFwd, GPIO.OUT) 
GPIO.setup(rightBckwd, GPIO.OUT) 
	
@app.route("/")
def index():
  GPIO.output(leftFwd, GPIO.LOW)
  GPIO.output(leftBckwd, GPIO.LOW)
  GPIO.output(rightFwd, GPIO.LOW)
  GPIO.output(rightBckwd, GPIO.LOW)
#	templateData = {
#	 	'button'  : buttonSts,
#      		'senPIR'  : senPIRSts,
#      		'ledRed'  : ledRedSts,
#      		'ledYlw'  : ledYlwSts,
#      		'ledGrn'  : ledGrnSts,
#	}
#	return render_template('index.html', **templateData)
return render_template('index.html')
	
@app.route("/<action>")
def action(action):
   
  if action == "left":
    GPIO.output(leftFwd, GPIO.HIGH)
    GPIO.output(leftBckwd, GPIO.LOW)
    GPIO.output(rightFwd, GPIO.LOW)
    GPIO.output(rightBckwd, GPIO.HIGH)
  if action == "right":
    GPIO.output(leftFwd, GPIO.LOW)
    GPIO.output(leftBckwd, GPIO.HIGH)
    GPIO.output(rightFwd, GPIO.HIGH)
    GPIO.output(rightBckwd, GPIO.LOW)
  if action == "forward":
    GPIO.output(leftFwd, GPIO.HIGH)
    GPIO.output(leftBckwd, GPIO.LOW)
    GPIO.output(rightFwd, GPIO.HIGH)
    GPIO.output(rightBckwd, GPIO.LOW)
  if action == "backwards":
    GPIO.output(leftFwd, GPIO.LOW)
    GPIO.output(leftBckwd, GPIO.HIGH)
    GPIO.output(rightFwd, GPIO.LOW)
    GPIO.output(rightBckwd, GPIO.HIGH) 
   
#	templateData = {
#	      	'button'  : buttonSts,
#      		'senPIR'  : senPIRSts,
#      		'ledRed'  : ledRedSts,
#      		'ledYlw'  : ledYlwSts,
#      		'ledGrn'  : ledGrnSts,
#	}
#	return render_template('index.html', **templateData)
return render_trmplate('index.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
