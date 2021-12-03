import RPi.GPIO as GPIO          
from time import sleep


in1 = 8 
in2 = 10
enA = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)

motor = GPIO.PWM(enA, 1000)
motor.start(100)

control = ''
state = True
while state:
    if(GPIO.input(in1) == GPIO.HIGH):
        print("true")
    else:
        print("false")



    control = input()
    if(control == 's'):
        #stop
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        print("stop")

    if(control == 'f'):
        #forward
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        print("forward")
    
    if(control == 'b'):
        #forward
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        print("backward")

    if(control == 'q'):
        #quit
        state = False

    



print("THE END!")
