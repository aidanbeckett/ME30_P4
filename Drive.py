
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
# GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
in1 = 8 
in2 = 10
in3 = 16
in4 = 18
enA = 12
enB = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT) 
GPIO.output(enA,GPIO.HIGH)
GPIO.setup(enB,GPIO.OUT) 
GPIO.output(enB,GPIO.HIGH)
	
@app.route("/")
def index():
  #stop
  GPIO.output(in1,GPIO.LOW)
  GPIO.output(in2,GPIO.LOW)
  GPIO.output(in3,GPIO.LOW)
  GPIO.output(in4,GPIO.LOW)
  print("stop")
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
    print("left")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
  if action == "right":
    print("right")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
  if action == "forward":
    print("forward")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
  if action == "backwards":
    print("backward")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH) 
   
#	templateData = {
#	      	'button'  : buttonSts,
#      		'senPIR'  : senPIRSts,
#      		'ledRed'  : ledRedSts,
#      		'ledYlw'  : ledYlwSts,
#      		'ledGrn'  : ledGrnSts,
#	}
#	return render_template('index.html', **templateData)
  return render_template('index.html')

if __name__ == "__main__":
   app.run(host='http://10.245.86.142:5000', port=80, debug=True)
