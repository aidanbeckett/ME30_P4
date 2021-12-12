
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
step1 = 35
step2 = 36
step3 = 37
step4 = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT) 

GPIO.output(enA,GPIO.HIGH)
GPIO.setup(enB,GPIO.OUT) 
GPIO.output(enB,GPIO.HIGH)

delay = 0.0055
motorState = "down"

def setStep(w1, w2, w3, w4):
  GPIO.output(step1, w1)

#yoooooo
  GPIO.output(step2, w2)
  GPIO.output(step3, w3)
  GPIO.output(step4, w4)

def makeStepsUp(steps):
  for i in range(steps):
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)

def makeStepsDown(steps):
  for i in range(steps)
    setStep(1,0,0,1)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(1,0,1,0)
    time.sleep(delay)


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
  if action == "down":
    if motorState == "up":
      makeStepsDown(200)
    if motorState == "med":#Move the motor to the up postion based on its current location
      makeStepsDown(100)
    motorState = "down" #Set the motor state to down
  if action == "med":
    if motorState == "up":
      makeStepsDown(100)
    if motorState == "down": #Move the motor to the medium postion based on its current location
      makeStepsUp(100)
    motorState = "med" #Set the motor state to medium
  if action == "up":
    if motorState == "med":
      makeStepsUp(100)
    if motorState == "med": #Move the motor to the down postion based on its current location
      makeStepsUp(200)
    motorState = "up" #Set the motor state to up
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
