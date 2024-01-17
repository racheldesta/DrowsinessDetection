import RPi.GPIO as GPIO
import time

# Motor A
ENA = 18  # Enable Pin for Motor A
IN1 = 23  # Input Pin 1 for Motor A
IN2 = 24  # Input Pin 2 for Motor A

# Motor B
ENB = 25  # Enable Pin for Motor B
IN3 = 12  # Input Pin 1 for Motor B
IN4 = 16  # Input Pin 2 for Motor B

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def stop():
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def turn_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def turn_right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def set_speed(speed):
    speed = min(100, max(0, speed))  # limit speed between 0 to 100
    pwm_a = GPIO.PWM(ENA, 1000)
    pwm_b = GPIO.PWM(ENB, 1000)
    pwm_a.start(speed)
    pwm_b.start(speed)

def cleanup():
    GPIO.cleanup()

# Main program
try:
    setup()
    set_speed(50)  # Set the initial speed to 50%
    
    while True:
        direction = input("Enter the direction (F: Forward, B: Backward, L: Left, R: Right, S: Stop): ")
        
        if direction == 'F':
            forward()
        elif direction == 'B':
            backward()
        elif direction == 'L':
            turn_left()
        elif direction == 'R':
            turn_right()
        elif direction == 'S':
            stop()
            break  # Exit the loop if 'S' is entered
        else:
            print("Invalid direction. Please try again.")

except KeyboardInterrupt:
    stop()
    cleanup()
    print("Program stopped by user.")